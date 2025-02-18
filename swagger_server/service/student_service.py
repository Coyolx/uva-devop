import os
import tempfile
# from functools import reduce
# from tinydb import TinyDB, Query

from pymongo import MongoClient
from bson.objectid import ObjectId

mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(mongo_uri)
db = client["student_db"]
collection = db["students"]

db_dir_path = tempfile.gettempdir()
db_file_path = os.path.join(db_dir_path, "students.json")
# student_db = TinyDB(db_file_path)


def add(student=None):
    # queries = []
    # query = Query()
    # queries.append(query.first_name == student.first_name)
    # queries.append(query.last_name == student.last_name)
    # query = reduce(lambda a, b: a & b, queries)
    # res = collection.search(query)
    # if res:
    #     return 'already exists', 409
    #
    # doc_id = collection.insert(student.to_dict())
    # student.student_id = doc_id
    # return student.student_id

    if not student:
        return {'detail': 'Invalid student data', 'status': 400}, 400

    existing_student = collection.find_one({
        "first_name": student.first_name,
        "last_name": student.last_name
    })

    if existing_student:
        return {'detail': 'Student already exists', 'status': 409}, 409

    result = collection.insert_one(student.to_dict())
    student.student_id = str(result.inserted_id)  # Convert ObjectId to string
    return student.student_id, 201


# def get_by_id(student_id=None, subject=None):
#     print("oi")
#     student = student_db.get(doc_id=int(student_id))
#     if not student:
#         return 'not found', 404
#     student['student_id'] = student_id
#     return student

def get_by_id(student_id=None, subject=None):
    # student = collection.get(doc_id=int(student_id))
    # if not student:
    #     return {'detail': 'Student not found', 'status': 404, 'title': 'Not Found'}, 404
    # student['student_id'] = student_id
    # return student, 200

    if not student_id:
        return {'detail': 'Student ID required', 'status': 400}, 400

    try:
        student = collection.find_one({"_id": ObjectId(student_id)})
        if not student:
            return {'detail': 'Student not found', 'status': 404}, 404

        student.student_id = str(student['_id'])  # Ensure _id is string
        return student, 200

    except Exception as e:
        return {'detail': str(e), 'status': 400}, 400


def delete(student_id=None):
    # student = collection.get(doc_id=int(student_id))
    # if not student:
    #     return 'not found', 404
    # collection.remove(doc_ids=[int(student_id)])
    # return student_id

    if not student_id:
        return {'detail': 'Student ID required', 'status': 400}, 400

    try:
        result = collection.delete_one({"_id": ObjectId(student_id)})
        if result.deleted_count == 0:
            return {'detail': 'Student not found', 'status': 404}, 404

        return {'detail': f'Student {student_id} deleted'}, 200

    except Exception as e:
        return {'detail': str(e), 'status': 400}, 400
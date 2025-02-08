import connexion

from swagger_server.models.student import Student  # noqa: E501
from swagger_server.service.student_service import *
# import six
# from swagger_server import util



def add_student(body=None):  # noqa: E501
    """Add a new student

    Adds an item to the system # noqa: E501

    :param body: Student item to add
    :type body: dict | bytes

    :rtype: float
    """
    if connexion.request.is_json:
        body = Student.from_dict(connexion.request.get_json())  # noqa: E501
        return add(body)  # Assuming 'add' is defined in student_service

    return 500, 'error'


def delete_student(student_id):  # noqa: E501
    """Deletes a student

    delete a single student  # noqa: E501

    :param student_id: Unique identifier for the student object.
    :type student_id: float

    :rtype: object
    """
    if connexion.request.is_json:
        body = Student.from_dict(connexion.request.get_json())
        return delete(body.student_id)
    return 500, 'error'


def get_student_by_id(student_id):  # noqa: E501
    """gets student

    Returns a single student # noqa: E501

    :param student_id: the uid
    :type student_id: 

    :rtype: Student
    """
    if connexion.request.is_json:
        body = Student.from_dict(connexion.request.get_json())
        return get_by_id(body.student_id)

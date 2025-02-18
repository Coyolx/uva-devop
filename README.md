### UvA DevOps Exercises 2025

- `Resources` folder contains the exercises.

#### Exercise 01 (Docker, Kubernetes and Swagger)
- [Link for the Swagger playground](https://app.swaggerhub.com/apis/uva-5f3/Tutorial/1.0.0) (Exercise 01): this code is used to generate this repository.
The folder is generated automatically from Swagger. Two options are available to run Python Flask server:
1. Run it locally with an environment and IDE of our choice.
2. Run a containerised server with Docker.

###### Option 1 - Local server
_The tutorial explains it quite well._

###### Option 2 - Containerised server for the front-end
```sh
docker build --tag goncaloj/student_service # "goncaloj" is my Docker username. Find your own (please).
# Running it in dettached mode (-d) is optional.
docker run -it -p -d 8080:8080 goncaloj/student_service
```

We should be able to access the UI in Swagger through `localhost`:
http://localhost:8080/tutorial/1.0.0/ui/

###### Option 3 - Containerised server using `docker-compose.yml` file with MongoDB
```sh

```


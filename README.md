# API functionalities:

This is a task management backend API

- User can create and delete new projects
- User can create, update, and delete new tasks
- Tasks are assigned to the specific project
- User can see/read all created tasks and projects

## Running backend API using docker

Install [docker](https://docs.docker.com) and [docker compose](https://docs.docker.com/compose).

Then run the following cmd from the root folder

```bash
docker-compose up
```

This will start the backend to receive endpoint requests from the frontends.

## Running backend API manually

Please use the following steps to use API manually

1. Install [python 3.8](https://www.python.org/downloads) or higher
2. From the project root run `pipenv install` to install all dependencies
3. Then start pipenv by running `pipenv shell`
4. Then from [api](/backend/api/) directory run cmd `python run.py` or `python3 run.py` to start the app

## Usage

The backend API is running at http://localhost:8601

Go to any web browser and open `http://localhost:8601` to verify if the app is up and running

You should get the following message in the browser

`{'message': 'welcome to task management app'}`

## How to use API

This API provides the above-listed functionalities for projects and tasks

1. For creating/deleting a project user can send a post/put request to `http://localhost:8601/project` with JSON data like:

```bash
{"project_name": "project-1"}
```

2. For creating/updating task user can send a post/put request to `http://localhost:8601/task` with JSON data like:

```bash
{
     "task_name": "task-1",
     "task_description": "This is task 1",
     "project_name": "project-1"
}
```

Note: Tasks have to be assigned to a specific project so please create a project first, before creating a task

3. For deleting the project(i.e project with id 1) user can send a delete request to `http://localhost:8601/project/1`

Note: Deleting the project also deletes all tasks in that project

4. For deleting task(i.e task with id 2) user can send a delete request to `http://localhost:8601/task/2`

5. To get the list of all project-related information user can send get request to `http://localhost:8601/projects`

6. To get the list of all tasks related information user can send get request to `http://localhost:8601/tasks`

7. You can use [postman](https://www.postman.com/) or curl for sending endpoint requests

## Happy coding

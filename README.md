# API functionalities:
This is a task management backend API 

* User can create, read, update, delete new folders and tasks 
* Tasks are assigned to the folder
* User can add/update task descriptions 
* User can set different priorities to the tasks
* Different participants can be assigned to the tasks
* User can see when task is created


# Running backend API using docker
Install [docker](https://docs.docker.co) and [docker compose](https://docs.docker.com/compose/).

Then run the following cmd from the root folder

     docker-compose up or $ docker-compose -d to run in the background

This will start the backend to receive endpoint requests from the frontends.


# Running backend API manually  
Please use the following steps to use API manually 
1. Install [python 3.7](https://www.python.org/downloads/) or higher
2. Install and create new [conda](https://docs.conda.io/en/latest/miniconda.html) isolated env or [python virtual env](https://docs.python.org/3/tutorial/venv.html) 
3. Then from /backend run `pip install -r requirements.txt`. it will install all required dependency
4. From /backend run `test.py` for testing and `run.py` for API uses


# Usage

Backend is running at http://localhost:8601

To verify the backend is running do following

     curl http://localhost:8601

You should get the following response message

`{'message': 'welcome to task management app'}`


# How to use API

This API provides above listed functionalities for folders and tasks

1. For creating/updating folder user can send a post/put request to `http://localhost:8601/folder` with JSON data like:
     `{"folder_name" : "new folder"}`
2. For creating/updating task user can send a post/put request to `http://localhost:8601/task` with JSON data like:
     `{
     "task_name" : "task 1",
     "task_description" : "this is task 1",
     "task_priority" : "high",
     "task_participant" : ["developer 1 ", "developer 2"], 
     "folder_id" : "1"
     }`

3. Tasks are assigned to a specific folder so please create a folder before creating a task
4. For deleting the folder(i.e folder with id 1) user can send a delete request to `http://localhost:8601/folder/1`.
   Note: Deleting folder also deletes all tasks in that folder
5. For deleting task(i.e task with id 2) user can send a delete request to `http://localhost:8601/task/2`
6. To get the list of all tasks related information user can send get request to `http://localhost:8601/task`
7. Use [postman](https://www.postman.com/) or curl for sending endpoint requests

## Happy coding 

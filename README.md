# Simple Task Manager API

This is a simple Django Rest Framework with basic CRUD operations. 

> Note: Although this project required the project and app name to be
> same, but I have named the app `taskapp` to avoid errors.

## Setup
The first thing to do is to clone the repository:

    git clone https://github.com/Kunnaalsoni/taskmanager.git
    cd taskmanager

Create a virtual environment to install dependencies in and activate it:

    virtualenv env
    source env/bin/activate

Then install the dependencies:

    (env)$ pip install -r requirements

Once  `pip`  has finished downloading the dependencies, setup the migration, this project currently uses the default sqlite3

    (env)$ cd project
    (env)$ python manage.py migrate
    (env)$ python manage.py makemigrations taskapp
    (env)$ python manage.py migrate
    
Then, setup a superuser account to generate some dummy data:

    (env)$ python manage.py createsuperuser

follow the prompts to create a superuser

Functional Endpoints:

 1. Retrieve a list of all tasks: 
	  `$ curl -X GET http://127.0.0.1:8000/api/tasks/`
 2. Create a new task:

    >       $curl --location '127.0.0.1:8000/api/tasks/' \
    >      --header 'Content-Type: application/json' \
    >      --data  '{
    >      "title": "Demo task 2",
    >      "description": "demo",
    >      "status": "Active"
    >      }

3. Retrieve a single task by its ID:
 `$ curl --location "127.0.0.1:8000/api/tasks/1/"`

4. Update a task:
    > curl --location --request PATCH '127.0.0.1:8000/api/tasks/1/' \
    > --header 'Content-Type: application/json' \
    > --data '{       
    >         "status": "InActive" }'

5. Delete a task:

    > curl --location --request DELETE '127.0.0.1:8000/api/tasks/1/' \
    > --header 'Content-Type: application/json' \
    > --data '{       
    >         "status": "InActive" }'

from flask import Blueprint, request
from models import ListToDo, todos
from datetime import datetime

#############################################
## USE THIS FILE TO DEFINE ANY Routes
## Create Sub Blueprints as needed
#############################################

home = Blueprint("home", __name__)

@home.get("/")
def home_home():
    return {"home": "this is the home route"}


@home.get("/todo")
def home_todo():
    return {"todos": tuple(map(lambda td: td.__dict__, todos))}


@home.get("/todo/<id>")
def home_todo_id(id):
    id = int(id)
    return todos[id].__dict__


@home.post("/todo")
def home_todo_create():
    body = request.json
    todo = ListToDo(
        body["title"],
        body["description"],
        body["finished_at"],
        body["created_at"],
        body["updated_at"],
        body["deleted_at"])

    # todo.created_at = datetime.now()

    todos.append(todo)
    return todo.__dict__


@home.route("/todo/<id>", methods=["PUT", "PATCH"])
def home_todo_update(id):
    id = int(id)
    body = request.json
    todo = todos[id]

    todo.title = body["title"]
    todo.description = body["description"]
    todo.finished_at = body["finished_at"]
    todo.created_at = body["created_at"]
    todo.updated_at = body["updated_at"]
    todo.deleted_at = body["deleted_at"]

    return todo.__dict__


@home.delete("/todo/<id>")
def home_todo_delete(id):
    id = int(id)
    todo = todos.pop(id)

    todo.deleted_at = datetime.now()
    return todo.__dict__


from datetime import datetime
from ariadne import convert_kwargs_to_snake_case
from mongoengine import Document
from mongoengine.fields import(StringField,ListField,ReferenceField)
from api import db
from api.models import Todo


@convert_kwargs_to_snake_case
def resolve_create_todo(obj, info, description, completed, due_date):
    try:
        meta={'collection': 'todo'}
        todo = Todo(
        description=description, completed=False, due_date=due_date
        )
        todo.save()
        payload = {
            "success": True,
            "todo": todo.to_dict()
        }
    except ValueError:  # date time errors
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }

    return payload


@convert_kwargs_to_snake_case
def resolve_mark_done(obj, info, todo_id):
    try:
        todo=Todo.objects.with_id(todo_id)
        meta={'collection': 'todo'}
        todo.completed = True
        todo.save()
        payload = {
            "success": True,
            "todo": todo.to_dict()
        }
    except AttributeError as error:
        payload = {
            "success": False,
            "errors":  [f"Todo matching id {todo_id} was not found"]
        }

    return payload


@convert_kwargs_to_snake_case
def resolve_delete_todo(obj, info, todo_id):
    try:
        meta={'collection': 'todo'}
        todo=Todo.objects.with_id(todo_id)
        todo.delete()
        todo.save()
        payload = {"success": True}

    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Todo matching id {todo_id} not found"]
        }
    return payload


@convert_kwargs_to_snake_case
def resolve_update_due_date(obj, info, todo_id, new_date):
    try:
        todo=Todo.objects.with_id(todo_id)
        if todo:
            todo.due_date = new_date
            todo.save()
        payload = {
            "success": True,
            "todo": todo.to_dict()
        }

    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": [f"Todo matching id {todo_id} not found"]
        }
    return payload

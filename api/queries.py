from ariadne import convert_kwargs_to_snake_case
from mongoengine import ObjectIdField
from .models import Todo



def resolve_todos(obj, info):
    try:
        todos = [todo.to_dict() for todo in Todo.objects.all()]
        payload = {
            "success": True,
            "todos": todos
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def resolve_todo(obj, info, id):
    try:        
        todo=Todo.objects.with_id(id)
        payload = {
            "success": True,
            "todo": todo.to_dict()
        }

    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": [f"Todo matching id {id} not found"]
        }

    return payload

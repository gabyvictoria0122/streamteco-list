from ..models import Todo


def add_todo(new_task):
    todo = Todo(description=new_task)
    todo.save()
    return todo.to_dict_json()

def edit_todo(id):
    edit = Todo.objects.get(id=task_id)
    edit.description = "Palavra que editei"
    edit.save()
    return edit.to_dict_json()


def list_todos():
    todos = Todo.objects.all()
    return [todo.to_dict_json() for todo in todos]

def remove_todos(task_id):
    Todo.objects.get(id=task_id).delete()
    return task_id
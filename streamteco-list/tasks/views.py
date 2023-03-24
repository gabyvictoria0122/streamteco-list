# coding: utf-8
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..commons.django_views_utils import ajax_login_required
from .service import todo_svc


@csrf_exempt
@ajax_login_required
def add_todo(request):
    todo = todo_svc.add_todo(request.POST["description"])
    return JsonResponse(todo)

def edit_todo(request, id):
    get_todo = todo_svc.edit_todo(request.POST["taskId"])
    return JsonResponse(get_todo)


@ajax_login_required
def list_todos(request):
    todos = todo_svc.list_todos()
    return JsonResponse({"todos": todos})


@ajax_login_required
def remove_todos(request):
    todo_id = todo_svc.remove_todos(request.POST["taskId"])
    return JsonResponse({"todo_id": todo_id})

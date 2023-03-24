from django.urls import path

from . import views

urlpatterns = [
    path("add", views.add_todo),
    path("list", views.list_todos),
    path("delete", views.remove_todos),
    path("edit/<int:id>", views.edit_todo),
]

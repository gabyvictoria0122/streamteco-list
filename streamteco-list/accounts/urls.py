from django.urls import path
from .views import views

from . import views

urlpatterns = [
    path('login', views.login),
    path('logout', views.logout),
    path('whoami', views.whoami),
    path('registrar', views.registrar),
]

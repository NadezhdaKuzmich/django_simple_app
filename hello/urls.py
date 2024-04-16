from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("user", views.user, name="user"),
    path("python", views.python, name="python"),
    path("<str:name>", views.greet, name="greet")
]

from django.urls import path

from . import views

app_name = "note"

urlpatterns = [
    path("", views.index, name="index"),
    path("noteCreate", views.noteCreate, name="noteCreate"),
    path("signup", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout", views.logout, name="logout"),
]
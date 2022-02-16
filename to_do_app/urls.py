from tkinter import N
from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path("login/",views.login_page,name="login"),
    path("logout/",views.logout_user,name="logout"),
    path("register/",views.register_page,name="register"),
    path("update_task/<str:pk>/",views.update_task,name="update_task"),
    path("delete_task/<str:pk>/",views.delete_task,name="delete_task"),
    path("statement/<str:pk>/",views.statement,name="statement"),
]

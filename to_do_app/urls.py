from tkinter import N
from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path("login/",views.login_page,name="login"),
    path("logout/",views.logout_user,name="logout"),
    path("register/",views.register_page,name="register"),
]

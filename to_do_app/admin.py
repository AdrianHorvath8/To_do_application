import imp
from re import T
from django.contrib import admin

# Register your models here.
from .models import Task

admin.site.register(Task)
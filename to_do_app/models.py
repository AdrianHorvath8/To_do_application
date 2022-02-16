from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    body=models.TextField()
    statement=models.BooleanField(default=False)
    #deathline=
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body

    class Meta:
        ordering=["-updated","-created"]

    
from django.db import models
from users.models import CustomUser


class Project(models.Model):
    name = models.CharField(verbose_name='Project Name', unique=True, max_length=64)
    repo_link = models.URLField(verbose_name='Repository Link', blank=True, null=True)
    users = models.ManyToManyField(CustomUser)

    def __str__(self):
        return f'Project {self.name}'


class ToDo(models.Model):
    text = models.TextField(verbose_name='ToDo text')
    created_date = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name='Created at', auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ManyToManyField(CustomUser)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'ToDoList {self.text}, created at {self.created_date}'


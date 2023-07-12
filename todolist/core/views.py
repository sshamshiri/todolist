from django.shortcuts import render
from django.views import generic
from .models import Task

class TaskList(generic.ListView):
    model = Task
    template_name = 'core/task_list.html'
    context_object_name = 'tasks'

class TaskDetail(generic.DetailView):
    model = Task
    template_name = 'core/task_detail.html'
    context_object_name = 'task'
from django.shortcuts import render
from django.views import generic
from .models import Task
from django.urls import reverse_lazy

class TaskList(generic.ListView):
    model = Task
    template_name = 'core/task_list.html'
    context_object_name = 'tasks'

class TaskDetail(generic.DetailView):
    model = Task
    template_name = 'core/task_detail.html'
    context_object_name = 'task'

class TaskCreate(generic.CreateView):
    model = Task
    fields = '__all__'
    success_url =reverse_lazy('core:tasks')
    
class TaskUpdate(generic.UpdateView):
    model =Task
    fields = '__all__'
    success_url =reverse_lazy('core:tasks')

class TaskDelete(generic.DeleteView):
    model = Task
    context_object_name = 'task'
    success_url =reverse_lazy('core:tasks')

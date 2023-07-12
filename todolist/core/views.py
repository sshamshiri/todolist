from django.shortcuts import redirect
from django.views import generic
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class TaskList(generic.ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(user = self.request.user)
        # context['tasks'] = Task.objects.filter(complete = False).count()

        filter_value = self.request.GET.get('filterBy') or ''
        if filter_value:
             context['tasks'] =  context['tasks'].filter(title__icontains=filter_value)
        context['filter_value']=filter_value

        return context

class TaskDetail(generic.DetailView):
    model = Task
    template_name = 'core/task_detail.html'
    context_object_name = 'task'

class TaskCreate(LoginRequiredMixin,generic.CreateView):
    model = Task
    fields = ['title','description','complete']
    success_url =reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class TaskUpdate(LoginRequiredMixin,generic.UpdateView):
    model =Task
    fields = '__all__'
    success_url =reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin,generic.DeleteView):
    model = Task
    context_object_name = 'task'
    success_url =reverse_lazy('tasks')

class CustomLoginView(LoginView):
    template_name = 'core/login.html'
    fields = '__all__'
    redirect_authenticated_url = True

    # def get_success_url(self) -> str:
    #     return reverse_lazy('tasks')

class RegisterView(generic.FormView):
    template_name = 'core/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request , user)
        return super().form_valid(form)
    
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super().get(*args,**kwargs)
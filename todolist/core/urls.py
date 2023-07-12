from django.urls import path 
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.TaskList.as_view() , name='tasks'),
    path('task/<int:pk>', views.TaskDetail.as_view() , name='task'),

]

from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Task
from .form import TaskForm
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect

class TaskListView(ListView) :
    model = Task
    template_name = "home.html"
    context_object_name = "tasks"

class TaskCreateView(CreateView) :
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = "/"

@csrf_protect
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('task-list') 

    return redirect('task-list')  
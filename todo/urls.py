from django.urls import path
from . import views
from .views import TaskListView, TaskCreateView

urlpatterns = [
    path("", TaskListView.as_view(), name = "task-list"),
    path("create/", TaskCreateView.as_view(), name = "add-task"),
    path('task/<int:pk>/delete/', views.task_delete, name='task-delete'),
]
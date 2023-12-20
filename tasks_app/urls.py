from django.urls import path
from .views import create_task, update_task, show_tasks, delete_task, home
urlpatterns = [
    path("", home, name="home"),
    path("show_tasks/", show_tasks, name="show_tasks"),
    path('add/', create_task, name="add_task"),
    path('update/<int:id>/', update_task, name="update_task"),
    path('delete/<int:id>/', delete_task, name="delete_task"),
]

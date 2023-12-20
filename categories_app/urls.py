from django.urls import path
from .views import update_category, create_category
urlpatterns = [
    path('add/', create_category, name="add_category"),
    path('update/', update_category, name="update_category"),

]

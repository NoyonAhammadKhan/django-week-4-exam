from django.db import models
# from categories_app.models import Category
from categories_app.models import Category
# Create your models here.


class Task(models.Model):
    task_tittle = models.CharField(max_length=100, null=False)
    task_description = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return f"{self.task_tittle}"

from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50, null=False)

    def __str__(self) -> str:
        return f"{self.category_name}"

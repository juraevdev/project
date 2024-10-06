from django.db import models
from users.models import CustomUser


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=350, blank=True, null=True)
    price = models.PositiveIntegerField()
    slug = models.SlugField(blank=True, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
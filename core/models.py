from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=350, blank=True, null=True)
    price = models.PositiveIntegerField()
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name
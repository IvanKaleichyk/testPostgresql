from django.db import models


class Employee(models.Model):
    years = models.CharField(max_length=3)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

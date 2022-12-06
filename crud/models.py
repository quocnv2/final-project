from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

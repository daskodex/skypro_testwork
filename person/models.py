from django.db import models


# Create your models here.

class SimplePerson(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    salary = models.PositiveIntegerField(default=0)
    education = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    portfolio = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name

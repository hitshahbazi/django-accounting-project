from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=20, unique=True)
    family = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

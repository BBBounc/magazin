from django.conf import settings
from django.db import models
from django.utils import timezone


class Service(models.Model): 
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self):
        return self.title

class Contacts(models.Model):
    email = models.CharField(max_length=200)
    tg = models.CharField(max_length=200)

    def __str__(self):
        return self.email

class Portfolio(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to ='uploads/') 

    def __str__(self):
        return self.name

from django.conf import settings
from django.db import models
from django.utils import timezone


class Service(models.Model): 
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.CharField(max_length=200)

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

    def __str__(self):
        return self.name

class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return f"{self.portfolio.name} - Image {self.id}"
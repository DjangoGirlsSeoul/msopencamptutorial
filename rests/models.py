from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    rating = models.FloatField()
    image = models.URLField()
    createdAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

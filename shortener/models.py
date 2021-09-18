from django.db import models

# Create your models here.

class URL(models.Model):
    url = models.CharField(max_length=200, unique=True)
    short_url = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.url
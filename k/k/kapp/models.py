from django.db import models

# Create your models here.
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    location = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

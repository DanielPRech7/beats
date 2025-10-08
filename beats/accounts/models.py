from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    celular = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    
    email = models.EmailField(unique=True) 
    
    def __str__(self):
        return self.username
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#class User(AbstractUser):
#    pass


class Lecture(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    
    #fk = models.ForeignKey('app.model', on_delete=models.CASCADE)
    def __repr__(self):
        return self.name
    def __str__(self):
        return self.__repr__()
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

class Inquiry(models.Model):
    title = models.CharField(max_length=64, verbose_name='Tittel', blank=True)
    description = models.TextField(verbose_name='Beskrivelse')
    name = models.CharField(max_length=64, verbose_name='Ditt navn')
    email = models.EmailField(null=True, verbose_name='Din epost')

    def __repr__(self):
        return self.name
    def __str__(self):
        return self.__repr__()
from django.db import models
from django.urls import reverse

class student(models.Model):
   name=models.CharField(max_length=128)
   mail=models.CharField(max_length=64)
   mobilenumber=models.IntegerField()
   def __str__(self):
     return self.name
   def get_absolute_url(self):
     return reverse('detail',kwargs={'pk':self.pk})

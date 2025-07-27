from django.db import models
from django.shortcuts import render



class format(models.Model):
    first_Name = models.CharField(max_length= 100, default=None)
    last_name = models.CharField(max_length=100, default= None )
    father_name =models.CharField(max_length=100, default=None)
    mother_name = models.CharField(max_length=100, default=None)
    dob = models.DateField(default=None)
    address = models.CharField(max_length= 200, default=None)
    phone = models.IntegerField(default=None)
    
    #def __str__(self):
        #return self.last_name
    
    
    
# Create your models here.

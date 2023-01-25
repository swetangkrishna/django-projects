from statistics import mode
from django.db import models

# Create your models here.

from datetime import date
from email.policy import default
from enum import unique
from time import time
from unittest.util import _MAX_LENGTH
from django.db import models
import uuid

from pyautogui import PRIMARY

    
class products(models.Model):
    DEPARTMENT_TYPE = (
        ('two', 'Pharma'),
        ('one', 'vet'),
    )
    
    name = models.CharField(max_length=200, unique=True, editable = False, primary_key=True)
    department = models.CharField(max_length=200, choices=DEPARTMENT_TYPE)
    launchdate = models.DateField(date)
    quantity =  models.CharField(max_length=200)
    

    def __str__(self):
        return self.name



class review(models.Model):
    Manufacturer_opt = (
        ('one', 'Sri_Ram_Healthcare_Pvt_Ltd'),
        ('two', 'Ultra_Drugs'),
        ('three', 'Prosperity'),
    )
    
    DEPARTMENT_TYPE = (
        ('two', 'Pharma'),
        ('one', 'vet'),
    )
    manufacturer = models.CharField(max_length=200, choices=Manufacturer_opt)
    prod = models.ForeignKey(products, on_delete=models.CASCADE)
    description = models.CharField(max_length=2000)
    composition = models.CharField(max_length=200)
    storage = models.CharField(max_length=200)
    name = models.CharField(max_length=200, unique=True, editable = False, primary_key=True)
    department = models.CharField(max_length=200, choices=DEPARTMENT_TYPE, default=1)
    def __str__(self):
        return self.manufacturer




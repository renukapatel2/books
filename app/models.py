from django.db import models

# Create your models here.
class seller(models.Model):
    fname = models.CharField(max_length=255,default="Firstname")
    lname = models.CharField(max_length=255,default="Lastname")
    email = models.EmailField(unique=True)
    passwd = models.CharField(max_length=255,default="Password")
    
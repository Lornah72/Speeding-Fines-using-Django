from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Drivers(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id_user = models.IntegerField()
    license_plate = models.CharField(max_length=100)
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    email  = models.CharField(max_length=100)
    phone_no =  models.IntegerField()

class Officer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id_officer = models.IntegerField()
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    email  = models.CharField(max_length=100)
    phone_no =  models.IntegerField()
    

    def __str__(self):
        return self.user.username






# Create your models here.

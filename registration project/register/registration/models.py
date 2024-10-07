from django.db import models

class user(models.Model):
    First_name=models.CharField(max_length=200)
    L_name=models.CharField(max_length=200)
    user_id=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    occupation=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    department=models.CharField(max_length= 10,default='SOME STRING')
    working=models.BooleanField(default=True)

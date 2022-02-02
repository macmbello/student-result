from django.db import models


class Profile(models.Model):
    fname = models.CharField(max_length=20)
    sname = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    reg_no = models.CharField(max_length=16, primary_key=True)
    email = models.EmailField(max_length=30)
    address = models.CharField(max_length=100)
    dob = models.DateField()
    picture = models.ImageField()
    
    
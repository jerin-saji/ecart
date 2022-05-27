from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProfileModel(models.Model):
    GENDER_CHOICES = (
        ("M","Male"),("F","Female"),("Others","Others")
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=14,default=0)
    image = models.ImageField(upload_to='image/user/', default='default/product.png')
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


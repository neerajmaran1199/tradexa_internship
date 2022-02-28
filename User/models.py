from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class User(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     email = models.EmailField()
#     password= models.CharField(max_length=200)
#     username = models.CharField(max_length=200)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True )
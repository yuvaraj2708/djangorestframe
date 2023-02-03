from django.db import models

# Create your models here.
class Profiles(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    phonenumber=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=200,null=True)
    status=models.CharField(max_length=200,null=True)
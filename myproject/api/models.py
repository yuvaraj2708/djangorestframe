from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profiles(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    phonenumber=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=200,null=True)
    status=models.CharField(max_length=200,null=True)


class Login(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE, null=True ,blank=True)
    auth_token = models.CharField(max_length=100 , null=True ,blank=True)
    is_verified = models.BooleanField(default=False, null=True ,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True ,blank=True)
    
    class Meta:
        db_table ='LOGIN'

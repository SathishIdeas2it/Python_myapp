from django.db import models    
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.  
class Post(models.Model):
    title = models.CharField(max_length=50) 
    description = models.CharField(max_length=50)
    details = models.CharField(max_length=255)    
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,default='')
    created_on = models.DateField(auto_now_add=True,null=True)
    image = models.ImageField(upload_to='images/',default="",null=True)
    image1 = models.BinaryField(null=True)
    
def __str__(self):
    return self.title


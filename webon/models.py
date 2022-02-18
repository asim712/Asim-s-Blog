from datetime import datetime
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name

class Post(models.Model):
    img = models.ImageField(upload_to = 'pics')
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.title
    
from django.db import models

# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=200)
    profile_pic = CloudinaryField('image')
    location = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    charge = models.IntegerField(blank=True)
    rating = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.name   

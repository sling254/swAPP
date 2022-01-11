from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)

    def save_location(self):
        self.save()

    def __str__(self):
        return self.name



class Driver(models.Model):
    name = models.CharField(max_length=200)
    photo = CloudinaryField("image",null=True)
    details = models.TextField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=200)
    phone_number = models.IntegerField( blank=True, null=True)
    charge = models.IntegerField(blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    
    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return f'{self.name} Driver'

    def create_driver(self):
        self.save()

    def delete_driver(self):
        self.delete()

    def update_driver(self):
        self.update()

    @classmethod
    def search_by_name(cls, search_term):
        driver = cls.objects.filter(name__icontains=search_term)
        return driver

    @classmethod
    def find_driver(cls, id):
        driver = cls.objects.get(id=id)
        return driver

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    efficiency_rate = models.IntegerField(default=0, blank=True, null=True)
    service_rate = models.IntegerField(default=0, blank=True, null=True)
    avarage_rate = models.IntegerField(default=0, blank=True, null=True)

    def _str_(self):
        return self.user.user

    def update_rating(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()

    def save_rating(self):
        self.save()

    def delete_rating(self):
        self.delete()

    def __str__(self):
        return self.driver

from django.db import models

# Create your models here.
class Employee_details(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='images')
    phone_number=models.CharField(max_length=13, blank=True)
    email=models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.first_name + " "+ self.last_name
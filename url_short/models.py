from django.db import models


# Create your models here.
class urlshortdb(models.Model):
    long_url_db = models.CharField(max_length=600)
    shorted_url_db = models.CharField(max_length=50)

    def __str__(self):
        return self.long_url_db

class contactus(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=40)
    messege = models.TextField(max_length=2000)

    def __str__(self):
        return self.email
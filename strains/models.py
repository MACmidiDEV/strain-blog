from django.db import models

# Create your models here.
class Strain(models.Model):
    name = models.CharField(max_length=254, default="")
    straintype = models.CharField(max_length=54, default="")
    description = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


    
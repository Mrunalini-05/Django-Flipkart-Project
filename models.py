from django.db import models

# models.py

class Product(models.Model):
    name = models.CharField(max_length=255 , null=True, blank=True)
    image =models.ImageField(upload_to='images/' , null=True, blank=True)
    description = models.TextField(null=True, blank=True)  
    price = models.DecimalField(max_digits=10, decimal_places=2 , null=True, blank=True)
    stock = models.IntegerField(null=True,blank=True)


    def __str__(self):
        return self.name

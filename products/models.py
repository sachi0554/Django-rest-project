from django.db import models

# Create your models here.
class product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=10000 , decimal_places=2)
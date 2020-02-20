from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False)


class Item(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=0)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    units = models.IntegerField()
    description = models.TextField(blank=True)

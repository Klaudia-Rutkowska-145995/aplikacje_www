from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Car(models.Model):
    brand = models.ForeignKey(Brand, related_name='cars', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    production_year = models.DecimalField(max_digits=65, decimal_places=0)
    price = models.DecimalField(max_digits=65, decimal_places=2)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

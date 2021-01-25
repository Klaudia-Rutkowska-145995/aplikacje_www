from django.db import models

class marka(models.Model):
    nazwaMarki = models.CharField(max_length=100)
    opis = models.TextField(blank=True)

    def __str__(self):
        return self.nazwaMarki

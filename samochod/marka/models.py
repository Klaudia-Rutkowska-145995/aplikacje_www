from django.db import models

class marka(models.Model):
    nazwaMarki = models.CharField(max_length=100)
    opis = models.TextField(blank=True)

    def __str__(self):
        return self.nazwaMarki

    class Meta:
        verbose_name = "Marka"
        verbose_name_plural = "Marki"

class samochod(models.Model):
    #nazwaMarki = models.CharField(max_length=100)
    marka = models.ForeignKey(marka, on_delete=models.CASCADE)
    nazwaSamochodu = models.CharField(max_length=50)
    opis = models.TextField(blank=True)
    rokProdukcji = models.DecimalField(max_digits=99999, decimal_places=0)
    cena = models.DecimalField(max_digits=99999, decimal_places=2)
    kolor = models.CharField(max_length=50)

    def __str__(self):
        return self.marka.nazwaMarki + ' ' + self.nazwaSamochodu
        #return self.nazwaSamochodu

    class Meta:
        verbose_name = "Samochod"
        verbose_name_plural = "Samochody"
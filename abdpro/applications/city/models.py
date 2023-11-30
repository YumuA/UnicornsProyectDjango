from django.db import models

class City(models.Model):
    idCity = models.CharField('idCity', max_length=3, primary_key=True)
    name = models.CharField('CityName', max_length=25)
    idcountry = models.CharField('idCountry', max_length=3)
    district = models.CharField('NameOfCity', max_length=25)
    population = models.BigIntegerField('Population')
    idTownHall = models.CharField('townhallid', max_length=3)

    class Meta:
        verbose_name = 'Name City'
        verbose_name_plural = 'Name Citys'
        ordering = ['name']
        unique_together = ('name', 'idcountry')

    def __str__(self):
        return f"{self.name} - {self.population} {str(self.idCity)}"

from django.db import models

class Country(models.Model):
    nombre_country = models.CharField('nombreCountry', max_length=25, null=False)
    id_country = models.CharField('idCountry', max_length=3, unique=True, null=False)
    continent_country = models.IntegerField('continentCountry', null=False)
    region_country = models.CharField('regionCountry', max_length=20, null=False)
    surface_country = models.DecimalField('countryArea', max_digits=10, decimal_places=2, null=False)
    indep_year_country = models.SmallIntegerField('indepCountry', null=True)
    population = models.IntegerField('populationCountry', null=False)
    life_expectancy = models.DecimalField('lifeExpectancy', max_digits=3, decimal_places=1, null=True)
    GNP = models.DecimalField('GNPCountry', max_digits=10, decimal_places=2, null=True)
    GNPold = models.DecimalField('GNPold', max_digits=10, decimal_places=2, null=True)
    localname = models.CharField('countryLocalname', max_length=45, null=False)
    government = models.CharField('countryGovernment', max_length=45, null=False)
    statehead = models.CharField('countryLeader', max_length=60, null=True)
    capital_country = models.IntegerField('capitalId', null=True)
    code2 = models.CharField('countryCode2', max_length=2, null=False)

    class Meta:
        verbose_name = 'Name Country'
        verbose_name_plural = 'Name Countries'
        ordering = ['nombre_country']
        unique_together = ('nombre_country', 'population')

    def __str__(self):
        return f"{self.nombre_country} - {self.population} {str(self.id_country)}"

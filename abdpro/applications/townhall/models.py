from django.db import models

class TownHall(models.Model):
    id_townhall = models.CharField('idTownHall', max_length=3, primary_key=True)
    mayor = models.CharField('Mayor name', max_length=25)
    councillor = models.CharField('active', max_length=25)

    class Meta:
        verbose_name = 'Name TownHall'
        verbose_name_plural = 'Name TownHalls'
        ordering = ['id_townhall']
        unique_together = ('id_townhall', 'mayor')

    def __str__(self):
        return f"{self.id_townhall} - {self.mayor} {str(self.id_townhall)}"

from django.db import models

class Language(models.Model):
    id_language = models.CharField('nombreLanguage', max_length=25, primary_key=True)
    percentage = models.BigIntegerField('PercentageOfSpeakers', unique=True)
    is_official = models.BooleanField('active', default=False)
    name_language = models.CharField('NameOfLanguage', max_length=25)

    class Meta:
        verbose_name = 'Name Language'
        verbose_name_plural = 'Name Languages'
        ordering = ['name_language']
        unique_together = ('name_language', 'percentage')

    def __str__(self):
        return f"{self.name_language} - {self.percentage} {str(self.id_language)}"

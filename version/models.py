from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Version(models.Model):
    product = models.CharField(max_length=100, verbose_name='product')
    version_number = models.IntegerField(verbose_name='version_number')
    version_name = models.CharField(max_length=100, verbose_name='version_name')
    version_status = models.BooleanField(default=True, verbose_name='version_status')

    def __str__(self):
        return self.version_name

    class Meta:
        verbose_name = 'version'
        verbose_name_plural = 'versions'

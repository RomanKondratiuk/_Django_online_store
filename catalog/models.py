from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    description = models.TextField(verbose_name='description')
    image = models.ImageField(upload_to='image/', verbose_name='image', **NULLABLE)
    category = models.TextField(verbose_name='category')
    purchase_price = models.IntegerField(**NULLABLE)
    date_of_creation = models.DateField(**NULLABLE)
    last_modified_date = models.DateField(**NULLABLE)

    def __str__(self):
        return f' {self.name} '

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='name ')
    description = models.TextField(verbose_name='description')

    def __str__(self):
        return f' {self.name}'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('name',)



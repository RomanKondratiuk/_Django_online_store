from django.db import models
from django.db.models import CASCADE

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    description = models.TextField(verbose_name='description')
    image = models.ImageField(upload_to='image/', verbose_name='image', **NULLABLE)
    category = models.TextField(verbose_name='category')
    purchase_price = models.IntegerField(**NULLABLE)
    date_of_creation = models.DateField(**NULLABLE)
    last_modified_date = models.DateField(**NULLABLE)
    sign_publication = models.BooleanField(default=False, verbose_name='publication sign', **NULLABLE)

    owner = models.ForeignKey(User, on_delete=CASCADE, **NULLABLE, verbose_name='owner')

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

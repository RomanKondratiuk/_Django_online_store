from django.db import models

NULLABLE = {'blank': True, 'null': True}


class BlogPost(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    slug = models.CharField(max_length=150, verbose_name='slug')
    content = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='image/', verbose_name='изображение', **NULLABLE)
    date_of_creation = models.DateField(verbose_name='дата создания')
    sign_publication = models.BooleanField(verbose_name='признак публикации')
    number_of_views = models.IntegerField(verbose_name='количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'




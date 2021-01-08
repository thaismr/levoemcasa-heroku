from django.db import models
from django.conf import settings
from django.utils.text import slugify
# from categories.models import Category
from store.models import Store
from utils import img_utils


# Create your models here.
class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.DO_NOTHING, verbose_name='Loja')
    name = models.CharField(max_length=50, verbose_name='Nome')
    slug = models.SlugField(unique=True)
    summary = models.TextField(max_length=450, verbose_name='Resumo')
    description = models.TextField(verbose_name='Descricao')
    image = models.ImageField(upload_to='store_images/%Y/%m/', blank=True, null=True, verbose_name='Imagem')
    price_from = models.FloatField(verbose_name='Preco de base')
    price_sale = models.FloatField(blank=True, null=True, verbose_name='Preco promocional')
    is_published = models.BooleanField(default=False, verbose_name='Publicar?')

    def __str__(self):
        return self.name

    '''
    Overwrite save() to add functionality.
    '''
    def save(self, *args, **kwargs):
        if not self.slug:
            # TODO: Check for uniqueness (consider product store)
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

        img_path = str(settings.MEDIA_ROOT + '/' + self.image.name)
        img_utils.img_resize(img_path, 800)


# Product Variations
class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    summary = models.CharField(max_length=255)
    image = models.ImageField(upload_to='store_images/%Y/%m/', blank=True, null=True)
    price = models.FloatField()
    price_sale = models.FloatField(blank=True, null=True)
    in_stock = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

    '''
    Overwrite save() to resize image.
    '''
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img_path = str(settings.MEDIA_ROOT + '/' + self.image.name)
        img_utils.img_resize(img_path, 800)


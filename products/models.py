from django.db import models
from django.conf import settings
# from categories.models import Category
from store.models import Store
from PIL import Image


# Create your models here.
class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    summary = models.TextField(max_length=450)
    description = models.TextField()
    image = models.ImageField(upload_to='store_images/%Y/%m/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    price_from = models.FloatField()
    price_sale = models.FloatField(blank=True, null=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @staticmethod       # doesn't alter the class
    def resize_image(img_name, new_width):
        img_path = str(settings.MEDIA_ROOT + '/' + img_name)
        img = Image.open(img_path)
        width, height = img.size

        if width > new_width:
            new_height = round(
                (new_width * height) / width
            )
            img = img.resize((new_width, new_height), Image.LANCZOS)

        img.save(img_path, optimize=True, quality=60)
        img.close()

    '''
    Overwrite save() to resize image.
    '''
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image(self.image.name, 800)


# Product Variations
class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    summary = models.TextField(max_length=450)
    image = models.ImageField(upload_to='store_images/%Y/%m/', blank=True, null=True)
    price = models.FloatField()
    price_sale = models.FloatField(blank=True, null=True)
    in_stock = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

    @staticmethod       # doesn't alter the class
    def resize_image(img_name, new_width):
        img_path = str(settings.MEDIA_ROOT + '/' + img_name)
        img = Image.open(img_path)
        width, height = img.size

        if width > new_width:
            new_height = round(
                (new_width * height) / width
            )
            img = img.resize((new_width, new_height), Image.LANCZOS)

        img.save(img_path, optimize=True, quality=60)
        img.close()

    '''
    Overwrite save() to resize image.
    '''
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image(self.image.name, 800)


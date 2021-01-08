from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Store(models.Model):
    admin = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    slogan = models.TextField(max_length=450)
    description = models.TextField()
    logo = models.ImageField(upload_to='store_logos/%Y/%m/', blank=True, null=True)
    image = models.ImageField(upload_to='store_images/%Y/%m/', blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    # class Meta:
    #     verbose_name = 'store'
    #     verbose_name_plural = 'stores'

    # type = models.CharField(
    #     default='V',
    #     max_length=1,
    #     choices=(
    #         ('V', 'Variado'),
    #         ('S', 'Simples'),
    #     )
    # )

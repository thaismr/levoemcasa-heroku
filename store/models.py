from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.contrib.auth.models import User
from utils import img_utils


# Create your models here.
class Store(models.Model):
    admin = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    slogan = models.CharField(max_length=250)
    description = models.TextField()
    logo = models.ImageField(upload_to='store_logos/%Y/%m/', blank=True, null=True)
    image = models.ImageField(upload_to='store_images/%Y/%m/', blank=True, null=True)

    def __str__(self):
        return self.name

    '''
    Overwrite save() to add functionality.
    '''
    def save(self, *args, **kwargs):
        if not self.slug:
            # TODO: Check for uniqueness
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

        # resize store logo
        logo_path = str(settings.MEDIA_ROOT + '/' + self.logo.name)
        img_utils.img_resize(logo_path, 80)

        # resize store front image
        img_path = str(settings.MEDIA_ROOT + '/' + self.image.name)
        img_utils.img_resize(img_path, 800)

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

from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.DO_NOTHING)
    slug = models.SlugField(unique=True)
    summary = models.CharField(max_length=255, verbose_name='Resumo')
    description = models.TextField(verbose_name='Descricao')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

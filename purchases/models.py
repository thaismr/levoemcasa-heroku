from django.db import models
from django.contrib.auth.models import User
from products.models import Product, Variation


# Create your models here.
class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    total = models.FloatField(default=0)
    status = models.CharField(
        default='C',
        max_length=1,
        choices=(
            ('A', 'Aprovado'),
            ('C', 'Criado'),
            ('E', 'Enviado'),
            ('F', 'Finalizado'),
            ('P', 'Pendente'),
            ('R', 'Reprovado'),
        )
    )

    def __str__(self):
        return f'Cart #{self.pk}'


class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Item #{self.pk}'

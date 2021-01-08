from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
import re


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    bio = models.TextField(max_length=800, blank=True, null=True)
    picture = models.ImageField(upload_to='profile_pics/%Y/%m/', blank=True, null=True)
    is_listed = models.BooleanField(default=False)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Perfil de Usuario'


class UserAddress(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    place_name = models.CharField(max_length=50, verbose_name='Nome do local')
    zip_code = models.CharField(max_length=8, verbose_name='CEP')
    street = models.CharField(max_length=50)
    number = models.CharField(max_length=5)
    complement = models.CharField(max_length=30)
    district = models.CharField(max_length=30, verbose_name='Bairro')
    city = models.CharField(max_length=30)
    state = models.CharField(
        max_length=2,
        default='RJ',
        choices=(
            ('RJ', 'Rio de Janeiro'),
        )
    )
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return self.place_name

    # TODO: Do custom form data validation (CPF, CEP, etc.)
    def clean(self):
        error_messages = {}

        if re.search(r'[^0-9]', self.zip_code) or len(self.zip_code) < 8:
            error_messages['zip_code'] = 'CEP invalido. Digite os 8 digitos do CEP.'

        if error_messages:
            raise ValidationError(error_messages)

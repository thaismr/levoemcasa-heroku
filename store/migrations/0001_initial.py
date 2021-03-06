# Generated by Django 3.1.5 on 2021-01-08 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slogan', models.TextField(max_length=450)),
                ('description', models.TextField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='store_logos/%Y/%m/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='store_images/%Y/%m/')),
                ('slug', models.SlugField(unique=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

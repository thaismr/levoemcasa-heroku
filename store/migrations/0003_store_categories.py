# Generated by Django 3.1.5 on 2021-01-09 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20210108_1853'),
        ('store', '0002_auto_20210108_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='categories',
            field=models.ManyToManyField(blank=True, to='categories.Category'),
        ),
    ]
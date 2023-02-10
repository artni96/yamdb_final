# Generated by Django 3.2 on 2022-12-31 13:49

import api.utils
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveSmallIntegerField(db_index=True, validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(api.utils.current_year)], verbose_name='год производства'),
        ),
    ]

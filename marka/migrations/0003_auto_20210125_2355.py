# Generated by Django 3.1.5 on 2021-01-25 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marka', '0002_auto_20210125_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='production_year',
            field=models.DecimalField(decimal_places=0, max_digits=9999),
        ),
    ]

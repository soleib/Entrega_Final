# Generated by Django 4.0.3 on 2022-04-25 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMrBlack', '0002_panchos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hamburguesas',
            name='salsaMrBlack',
            field=models.CharField(max_length=45, verbose_name='salsaMrBlack'),
        ),
    ]
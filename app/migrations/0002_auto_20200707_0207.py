# Generated by Django 3.0.8 on 2020-07-07 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pessoas',
            new_name='Produtos',
        ),
        migrations.AlterModelTable(
            name='produtos',
            table='produtos',
        ),
    ]

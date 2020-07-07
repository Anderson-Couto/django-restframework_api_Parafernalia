# Generated by Django 3.0.8 on 2020-07-07 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200707_1443'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='produtos',
            name='bdp_lte_25',
        ),
        migrations.AddConstraint(
            model_name='produtos',
            constraint=models.CheckConstraint(check=models.Q(base_discount_percent__lte=25.0), name='base_discount_max'),
        ),
    ]

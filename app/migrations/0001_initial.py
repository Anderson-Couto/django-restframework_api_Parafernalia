# Generated by Django 3.0.8 on 2020-07-08 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=400)),
                ('base_discount_percent', models.FloatField()),
            ],
            options={
                'db_table': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
            ],
            options={
                'db_table': 'Usuarios',
            },
        ),
        migrations.AddConstraint(
            model_name='produtos',
            constraint=models.CheckConstraint(check=models.Q(base_discount_percent__lte=25.0), name='base_discount_max'),
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-17 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='brands',
            field=models.ManyToManyField(blank=True, related_name='companies', to='company.brand', verbose_name='Бренды'),
        ),
    ]

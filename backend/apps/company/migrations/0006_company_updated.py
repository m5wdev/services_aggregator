# Generated by Django 4.0.5 on 2022-06-22 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_alter_company_brands'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

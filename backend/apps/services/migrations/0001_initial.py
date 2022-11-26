# Generated by Django 4.0.5 on 2022-06-15 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название Категории для услуги')),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children_category_service', to='services.categoryservice', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'Категория услуги',
                'verbose_name_plural': 'Категории услуг',
                'db_table': 'services_categories',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название услуги')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, verbose_name='Slug')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена (от)')),
                ('price_max', models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена (до)')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service', to='services.categoryservice', verbose_name='Категория услуги')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='company.company', verbose_name='Компания')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
                'db_table': 'services',
            },
        ),
    ]

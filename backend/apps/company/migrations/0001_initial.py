# Generated by Django 4.0.5 on 2022-06-15 10:07

import apps.company.models.brand
import apps.company.models.category
import apps.company.models.company
import apps.company.models.company_image
import django.core.validators
from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название бренда')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('logo', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=apps.company.models.brand.brand_logo_upload, verbose_name='Логотип')),
                ('popular', models.BooleanField(default=False, verbose_name='Популярный бренд')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
                'db_table': 'brands',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='e.g.: 3D-принтеры', max_length=255, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('declension_one_p', models.CharField(blank=True, help_text='e.g.: 3D-принтеров', max_length=255, null=True, verbose_name='Склонение')),
                ('logo', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=apps.company.models.category.category_logo_upload, verbose_name='Логотип')),
                ('important', models.BooleanField(default=False, help_text='Отображать ли в брендах и т д', verbose_name='Важное')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Активная')),
                ('name', models.CharField(max_length=255, verbose_name='Название компании')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, verbose_name='Slug')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email')),
                ('url', models.URLField(blank=True, max_length=255, null=True, verbose_name='Сайт')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Телефон')),
                ('logo', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=apps.company.models.company.company_logo_upload, verbose_name='Логотип компании')),
                ('courier_departure', models.BooleanField(default=False, verbose_name='Выезд курьера')),
                ('master_departure', models.BooleanField(default=False, verbose_name='Выезд мастера')),
                ('free_diagnostics', models.BooleanField(default=False, verbose_name='Бесплатная диагностика')),
                ('quick_repair', models.BooleanField(default=False, verbose_name='Срочный ремонт')),
                ('pay_after_repair', models.BooleanField(default=False, verbose_name='Ремонт без предоплаты')),
                ('own_warehouse', models.BooleanField(default=False, verbose_name='Собственный склад запчастей')),
                ('free_parking', models.BooleanField(default=False, verbose_name='Бесплатная парковка')),
                ('fix_price', models.BooleanField(default=False, verbose_name='Фиксированная стоимость ремонта')),
                ('cash_pay', models.BooleanField(default=False, verbose_name='Оплата наличными')),
                ('card_pay', models.BooleanField(default=False, verbose_name='Оплата картой')),
                ('owner_register', models.BooleanField(default=False, verbose_name='Владелец зарегистрирован')),
                ('min_price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Минимальная цена')),
                ('max_price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Максимальная цена')),
                ('number_of_employees', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество работников')),
                ('year_of_foundation', models.CharField(blank=True, max_length=255, null=True, verbose_name='Год основания')),
                ('ya_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='YA_ID')),
                ('ya_categories', models.TextField(blank=True, null=True, verbose_name='YA_Categories')),
                ('ya_services', models.TextField(blank=True, null=True, verbose_name='YA_Services')),
                ('is_promo', models.BooleanField(default=False, verbose_name='Промо')),
                ('promo', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
                'db_table': 'companies',
            },
        ),
        migrations.CreateModel(
            name='CompanyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=apps.company.models.company_image.company_image_upload, verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Компания Изображение',
                'verbose_name_plural': 'Компании Изображения',
                'db_table': 'companies_images',
            },
        ),
        migrations.CreateModel(
            name='OftenRepair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название услуги')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Часто ремонтируем',
                'verbose_name_plural': 'Часто ремонтируемые',
                'db_table': 'company_often_repair',
            },
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Активная')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название мастерской')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Телефон')),
                ('office', models.CharField(blank=True, max_length=255, null=True, verbose_name='Офис')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('address_with_city', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес (с городом)')),
                ('work_time', models.TextField(blank=True, null=True, verbose_name='Время работы')),
                ('latitude', models.CharField(blank=True, max_length=255, null=True, verbose_name='Широта')),
                ('longitude', models.CharField(blank=True, max_length=255, null=True, verbose_name='Долгота')),
                ('moderated', models.BooleanField(default=False, verbose_name='Модерированно')),
            ],
            options={
                'verbose_name': 'Мастерская',
                'verbose_name_plural': 'Мастерские',
                'db_table': 'company_points',
            },
        ),
    ]

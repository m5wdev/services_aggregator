# Generated by Django 4.0.5 on 2022-06-15 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='e.g: Москва', max_length=255, unique=True, verbose_name='Город')),
                ('declension_p', models.CharField(blank=True, help_text='e.g: Москве', max_length=255, null=True, verbose_name='Находится в')),
                ('declension_r', models.CharField(blank=True, help_text='e.g: Москвы', max_length=255, null=True, verbose_name='Работает из')),
                ('v_declension_p', models.CharField(blank=True, help_text='e.g: в Москве', max_length=255, null=True, verbose_name='Находится где')),
                ('lower_latitude', models.CharField(blank=True, max_length=150, null=True, verbose_name='Нижняя широта')),
                ('lower_longitude', models.CharField(blank=True, max_length=150, null=True, verbose_name='Нижняя долгота')),
                ('upper_latitude', models.CharField(blank=True, max_length=150, null=True, verbose_name='Верхняя широта')),
                ('upper_longitude', models.CharField(blank=True, max_length=150, null=True, verbose_name='Верхняя долгота')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'db_table': 'cities',
            },
        ),
        migrations.CreateModel(
            name='MetroLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название линии метро')),
                ('color', models.CharField(max_length=255, verbose_name='Цвет линии')),
            ],
            options={
                'verbose_name': 'Линия Метро',
                'verbose_name_plural': 'Метро (Линии)',
                'db_table': 'metro_lines',
            },
        ),
        migrations.CreateModel(
            name='Subdomain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(help_text='e.g.: moscow', max_length=255, unique=True, verbose_name='Поддомен')),
            ],
            options={
                'verbose_name': 'Поддомен',
                'verbose_name_plural': 'Поддомены',
                'db_table': 'subdomains',
            },
        ),
        migrations.CreateModel(
            name='MetroStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название станции метро')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='station_metro', to='city.city', verbose_name='Город')),
                ('metro_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='station_metro', to='city.metroline', verbose_name='Линия метро')),
            ],
            options={
                'verbose_name': 'Станция Метро',
                'verbose_name_plural': 'Метро (Станции)',
                'db_table': 'metro_stations',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='subdomain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='city.subdomain', verbose_name='Поддомен'),
        ),
    ]

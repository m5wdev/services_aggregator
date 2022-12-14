# Generated by Django 4.0.5 on 2022-06-15 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('meta_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Мета Заголовка')),
                ('meta_descr', models.TextField(blank=True, null=True, verbose_name='Мета Описания')),
                ('group_name', models.CharField(blank=True, choices=[('1', 'Политика конфиденциальности'), ('2', 'Условия и положения'), ('3', 'Новости')], default='1', max_length=255, null=True, verbose_name='Группа записи')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
                'db_table': 'blog',
            },
        ),
    ]

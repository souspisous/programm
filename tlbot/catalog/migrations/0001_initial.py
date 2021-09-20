# Generated by Django 3.1b1 on 2020-06-20 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, verbose_name='Название книги')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='Имя писателя')),
                ('last_name', models.CharField(max_length=150, verbose_name='Фамилия писателя')),
                ('book', models.ManyToManyField(to='catalog.Book')),
            ],
            options={
                'verbose_name': 'Писатель',
                'verbose_name_plural': 'Писатели',
            },
        ),
    ]

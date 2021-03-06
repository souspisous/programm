# Generated by Django 3.2.7 on 2021-09-19 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Категория коммикса')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Comics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название комикса')),
                ('comment', models.TextField(max_length=200, verbose_name='Комментарий')),
                ('grade', models.FloatField(default=0, verbose_name='Оценка')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comics_site.category')),
            ],
        ),
    ]

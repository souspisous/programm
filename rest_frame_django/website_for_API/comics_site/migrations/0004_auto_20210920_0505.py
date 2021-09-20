# Generated by Django 3.2.7 on 2021-09-20 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comics_site', '0003_alter_comics_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='comics',
            name='slug',
            field=models.SlugField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
    ]

# Generated by Django 3.2.7 on 2021-09-20 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comics_site', '0006_auto_20210921_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comics',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Доступность'),
        ),
        migrations.AlterField(
            model_name='comics',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='comics',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Обновлен'),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='img/%Y/%m/%d')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='images', to='comics_site.comics')),
            ],
        ),
    ]

# Generated by Django 2.0 on 2022-04-16 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_anotation'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date_publication',
            field=models.DateField(default='2012-12-12', verbose_name='Дата приема'),
            preserve_default=False,
        ),
    ]

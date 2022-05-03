# Generated by Django 2.1.5 on 2022-04-16 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_date_publication'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='file',
            field=models.FileField(default=1, upload_to='', verbose_name='Файл'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default=1, upload_to='images', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]

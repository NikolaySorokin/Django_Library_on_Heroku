# Generated by Django 3.1 on 2020-08-07 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0003_auto_20200808_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='took_copy',
            field=models.ManyToManyField(blank=True, related_name='borrowed_books', to='p_library.Friend', verbose_name='одолжен экземпляр книги'),
        ),
    ]

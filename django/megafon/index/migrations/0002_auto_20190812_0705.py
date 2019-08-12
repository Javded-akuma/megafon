# Generated by Django 2.2.4 on 2019-08-12 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/'),
        ),
        migrations.AlterField(
            model_name='author',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Описание автора'),
        ),
        migrations.AlterField(
            model_name='books',
            name='description',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Описание книги'),
        ),
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/'),
        ),
        migrations.AlterField(
            model_name='books',
            name='series',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Серия'),
        ),
    ]
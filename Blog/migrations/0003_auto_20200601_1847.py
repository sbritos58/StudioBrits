# Generated by Django 3.0.6 on 2020-06-01 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='Post', verbose_name='Imagen'),
        ),
    ]

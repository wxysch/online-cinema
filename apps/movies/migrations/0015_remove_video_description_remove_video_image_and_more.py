# Generated by Django 4.1 on 2022-08-26 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0014_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='description',
        ),
        migrations.RemoveField(
            model_name='video',
            name='image',
        ),
        migrations.RemoveField(
            model_name='video',
            name='title',
        ),
    ]

# Generated by Django 4.1 on 2022-08-26 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0015_remove_video_description_remove_video_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1 on 2022-08-22 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_user_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default=1, upload_to='profile_image/'),
            preserve_default=False,
        ),
    ]
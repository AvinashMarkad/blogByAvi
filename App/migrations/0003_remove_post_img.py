# Generated by Django 4.2.5 on 2024-03-08 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_post_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='img',
        ),
    ]

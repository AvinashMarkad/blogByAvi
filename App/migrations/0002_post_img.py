# Generated by Django 4.2.5 on 2024-03-08 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]

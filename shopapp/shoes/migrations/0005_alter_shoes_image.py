# Generated by Django 5.1.3 on 2024-11-26 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0004_alter_shoes_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoes',
            name='image',
            field=models.ImageField(default='shoes_images/default.jpg', upload_to='shoes_images/'),
        ),
    ]

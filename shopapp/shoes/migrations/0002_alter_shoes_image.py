# Generated by Django 5.1.3 on 2024-12-06 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoes',
            name='image',
            field=models.ManyToManyField(to='shoes.images'),
        ),
    ]

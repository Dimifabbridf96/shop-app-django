# Generated by Django 5.1.3 on 2024-12-09 16:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0002_clothes_material_alter_clothes_brand_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='gender',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Unisex', 'Unisex')], default='Unisex', max_length=20),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='clothes_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.clothes')),
            ],
            options={
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.AddField(
            model_name='clothes',
            name='image',
            field=models.ManyToManyField(to='clothes.images'),
        ),
    ]

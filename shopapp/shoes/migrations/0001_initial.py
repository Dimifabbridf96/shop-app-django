# Generated by Django 5.1.3 on 2024-11-22 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('size', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('stock', models.IntegerField(default=0)),
                ('material', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Shoes',
            },
        ),
    ]
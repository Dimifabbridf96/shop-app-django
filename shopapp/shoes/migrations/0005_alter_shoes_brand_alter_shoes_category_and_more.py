# Generated by Django 5.1.3 on 2024-12-09 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0004_alter_shoes_brand_alter_shoes_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoes',
            name='brand',
            field=models.CharField(choices=[('Adidas', 'Adidas'), ('Nike', 'Nike'), ('Reebok', 'Reebok'), ('Puma', 'Puma'), ('New Balance', 'New Balance'), ('Asics', 'Asics'), ('Other', 'Other')], max_length=20),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='category',
            field=models.CharField(choices=[('Sportswear', 'Sportswear'), ('Casualwear', 'Casualwear'), ('Childrenwear', 'Childrenwear'), ('Accessories', 'Accessories'), ('Other', 'Other')], max_length=20),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='color',
            field=models.CharField(choices=[('Black', 'Black'), ('White', 'White'), ('Red', 'Red'), ('Blue', 'Blue'), ('Green', 'Green'), ('Yellow', 'Yellow'), ('Purple', 'Purple'), ('Orange', 'Orange'), ('Pink', 'Pink'), ('Brown', 'Brown'), ('Gray', 'Gray'), ('Other', 'Other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='gender',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Unisex', 'Unisex')], max_length=10),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='material',
            field=models.CharField(choices=[('Leather', 'Leather'), ('Canvas', 'Canvas'), ('Rubber', 'Rubber'), ('Synthetic fabrics', 'Synthetic fabrics'), ('Other', 'Other')], max_length=20),
        ),
    ]

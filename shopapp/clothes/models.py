from django.db import models

COLOR_CHOICES = (
    ('Black', 'Black'),
    ('White', 'White'),
    ('Red', 'Red'),
    ('Blue', 'Blue'),
    ('Green', 'Green'),
    ('Yellow', 'Yellow'),
    ('Purple', 'Purple'),
    ('Orange', 'Orange'),
    ('Pink', 'Pink'),
    ('Brown', 'Brown'),
    ('Gray', 'Gray'),
    ('Other','Other')
)

BRAND_CHOICES = (
    ('Adidas', 'Adidas'),
    ('Nike', 'Nike'),
    ('Reebok', 'Reebok'),
    ('Puma', 'Puma'),
    ('New Balance', 'New Balance'),
    ('Asics', 'Asics'),
    ('Other','Other')
)

CATEGORY_CHOICES = (
    ('Sportswear', 'Sportswear'),
    ('Casualwear', 'Casualwear'),
    ('Childrenwear', 'Childrenwear'),
    ('Accessories', 'Accessories'),
    ('Other','Other')
)

MATERIAL_CHOICES = (
    ('Cotton','Cotton'),
    ('Polyester','Polyester'),
    ('Leather','Leather'),
    ('Wool','Wool'),
    ('Synthetic fabrics', 'Synthetic fabrics'),
    ('Other','Other')
)

GENDER_CHOICES = (
    ('Men', 'Men'),
    ('Women', 'Women'),
    ('Unisex', 'Unisex')
    )

class Clothes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=20)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    material = models.CharField(max_length=20, choices=MATERIAL_CHOICES, default='Cotton')  # Added for material
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='Unisex')
    stock = models.IntegerField(default=0)
    image = models.ManyToManyField('Images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Clothes"

class Images(models.Model):
    article = models.ForeignKey(Clothes, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='clothes_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.article.name} - {self.id}"
    
    class Meta:
        verbose_name_plural = "Images"
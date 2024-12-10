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

CATEGORY_CHOICES =(
    ('Sportswear', 'Sportswear'),
    ('Casualwear', 'Casualwear'),
    ('Childrenwear', 'Childrenwear'),
    ('Accessories', 'Accessories'),
    ('Other','Other')
)

MATERIAL_CHOICES = (
    ('Leather', 'Leather'),
    ('Canvas', 'Canvas'),
    ('Rubber', 'Rubber'),
    ('Synthetic fabrics', 'Synthetic fabrics'),
    ('Other','Other')
)

GENDER_CHOICES = (
    ('Men', 'Men'),
    ('Women', 'Women'),
    ('Unisex', 'Unisex')
    )

class Shoes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=10)  # Changed to accommodate shoe sizes
    color = models.CharField(max_length=10, choices=COLOR_CHOICES)
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    stock = models.IntegerField(default=0)
    material = models.CharField(max_length=20, choices=MATERIAL_CHOICES)  # Added for shoe material
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)  # Added for gender (e.g., Men, Women, Unisex)
    image = models.ManyToManyField('Images')  # Updated to use ManyToManyField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Shoes"

class Images(models.Model):
    shoe = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shoe_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.shoe.name} - {self.id}"
    
    class Meta:
        verbose_name_plural = "Images"
    
class Slider(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='slider_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Sliders"

   

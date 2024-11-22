from django.db import models

class Shoes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=10)  # Changed to accommodate shoe sizes
    color = models.CharField(max_length=50)
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    stock = models.IntegerField(default=0)
    material = models.CharField(max_length=50)  # Added for shoe material
    gender = models.CharField(max_length=10)  # Added for gender (e.g., Men, Women, Unisex)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Shoes"

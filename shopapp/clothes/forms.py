from django import forms
from .models import Clothes

COLOR_CHOICES = (
    ('','All'),
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
    ('','All'),
    ('Adidas', 'Adidas'),
    ('Nike', 'Nike'),
    ('Reebok', 'Reebok'),
    ('Puma', 'Puma'),
    ('New Balance', 'New Balance'),
    ('Asics', 'Asics'),
    ('Other','Other')
)

CATEGORY_CHOICES = (
    ('','All'),
    ('Sportswear', 'Sportswear'),
    ('Casualwear', 'Casualwear'),
    ('Childrenwear', 'Childrenwear'),
    ('Accessories', 'Accessories'),
    ('Other','Other')
)

MATERIAL_CHOICES = (
    ('','All'),
    ('Cotton','Cotton'),
    ('Polyester','Polyester'),
    ('Leather','Leather'),
    ('Wool','Wool'),
    ('Synthetic fabrics', 'Synthetic fabrics'),
    ('Other','Other')
)

GENDER_CHOICES = (
    ('','All'),
    ('Men', 'Men'),
    ('Women', 'Women'),
    ('Unisex', 'Unisex')
    )

class ClothesFilterForm(forms.Form):
    brand = forms.ChoiceField(choices=BRAND_CHOICES, required=False)
    color = forms.ChoiceField(choices=COLOR_CHOICES ,required=False)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES ,required=False)
    material = forms.ChoiceField(choices=MATERIAL_CHOICES, required=False)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=False)

    def filter_clothes(self, queryset):
        brand = self.cleaned_data.get('brand')
        color = self.cleaned_data.get('color')
        category = self.cleaned_data.get('category')
        material = self.cleaned_data.get('material')
        gender = self.cleaned_data.get('gender')

        filters = {}

        if brand and brand != '':
            filters['brand'] = brand
        if color and color != '':
            filters['color'] = color
        if category and category != '':
            filters['category'] = category
        if material and material != '':
            filters['material'] = material
        if gender and gender != '':
            filters['gender'] = gender

        queryset = queryset.filter(**filters)

        return queryset
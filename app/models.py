from django.db import models

# Create your models here.

CATEGORY_CHOICES=(
    ('CR', 'Cure'),
    ('ML', 'Milk'),
    ('EG', 'Egg'),
    ('FR', 'Fruit'),
    ('VE', 'Vegetable'),
    ('GH','Ghee'),
    ('FL','Flour'),
    ('SP','Spice'),
    ('IC','Ice-Creams')
)

class product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title
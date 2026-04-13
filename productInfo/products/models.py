from django.db import models

class Category(models.Model):
    category_text = models.CharField(max_length=200)

    def __str__(self):
        return self.category_text
    
class Tag(models.Model):
    tag_text = models.CharField(max_length=100)

    def __str__(self):
        return self.tag_text

class Product(models.Model):
    product_text = models.CharField(max_length=200)
    description = models.TextField()

    # ForeignKey, many to one
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name="products"
    )

    # Many to Many
    tag = models.ManyToManyField(
        Tag,
        related_name="products"
    )

    def __str__(self):
        return self.product_text


    



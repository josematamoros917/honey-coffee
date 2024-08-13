from django.db import models
from django.utils import timezone

class Store(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    logo = models.ImageField(upload_to='logos/')
    description = models.TextField()
    mission = models.TextField()
    vision = models.TextField()
    strategic_objectives = models.TextField()
    organizational_culture = models.TextField()
    business_strategy = models.TextField()
    company_policies = models.TextField()

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products')
    categories = models.ManyToManyField(Category, related_name='products')

    def __str__(self):
        return self.name
    
class SocialMedia(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='social_media/')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='social_medias')
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class SocialMediaProduct(models.Model):
    link = models.URLField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='social_media_products')
    social_media = models.ForeignKey(SocialMedia, on_delete=models.CASCADE, related_name='social_media_products')

    def __str__(self):
        return f"{self.product.name} - {self.social_media.name}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name} - {self.email}'
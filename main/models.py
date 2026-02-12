from django.db import models
from django.utils.text import slugify
from django.core.validators import RegexValidator


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    category_image = models.ImageField(upload_to='category')


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="services"
    )

    phone_number = models.CharField(max_length=20)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    main_image = models.ImageField(upload_to='services/main/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)


    def __str__(self):
        return self.name
    

class ServiceImage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE,  related_name='images')
    image = models.ImageField(upload_to='services/extra/')

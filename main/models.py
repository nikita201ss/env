from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    category_image = models.ImageField(upload_to='category')


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

            original_slug = self.slug
            counter = 1
            while Category.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
                
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    class Meta:
            verbose_name = 'Category'           
            verbose_name_plural = 'Categories'

class Service(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="services"
    )

    phone_number = models.CharField(max_length=20)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    main_image = models.ImageField(upload_to='services/main/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    city = models.CharField(max_length=100, blank=True, verbose_name="Город")
    address = models.CharField(max_length=255, blank=True, verbose_name="Адрес")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

            original_slug = self.slug
            counter = 1
            while Service.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
    
    def get_location(self):
        if hasattr(self, 'city') and hasattr(self, 'address'):
            if self.city and self.address:
                return f"{self.city}, {self.address}"
            elif self.city:
                return self.city
            elif self.address:
                return self.address
        return self.location if hasattr(self, 'location') else ""
    

class ServiceImage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE,  related_name='images')
    image = models.ImageField(upload_to='services/extra/')

from django.contrib import admin
from .models import Category, Service, ServiceImage

class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'city', 'price']
    list_filter = ['category', 'city']
    search_fields = ['name', 'description', 'city', 'address']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ServiceImageInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    

admin.site.register(Category, CategoryAdmin)
admin.site.register(Service, ServiceAdmin)
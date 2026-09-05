from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}   # Предзаполнение slug по name

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available', 'created', 'updated']   # Показываемые в админке парметры
    list_filter = ['available', 'created', 'updated', 'category']   # Фильтрация в админке
    list_editable = ['price', 'available']   # Редактируемые параметры
    prepopulated_fields = {'slug': ('name',)}

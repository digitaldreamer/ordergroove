from django.contrib import admin
from django.db import models

from shop.products.models import Category, Product, ProductImage
from ordergroove.widgets import AdminImageWidget


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'site', 'parent', 'order', 'active')
    list_filter = ('site', 'active')
    search_fields = ('name', 'parent')
    prepopulated_fields = {'slug': ('name',)}
    exclude = ('site',)
    ordering = ('order',)


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1
    ordering = ('order',)

    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget},
    }


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'site', 'order', 'price', 'total_sold', 'created', 'modified', 'active')
    list_filter = ('site', 'active')
    search_fields = ('name', 'sku')
    prepopulated_fields = {'slug': ('name',)}
    exclude = ('site',)
    ordering = ('order',)
    filter_horizontal = ('categories',)
    inlines = (ProductImageInline,)
    readonly_fields = ('site', 'created', 'modified')
    fieldsets = (
        (None, {'fields': ('name', 'short_name', 'slug', 'sku', 'active', 'featured', 'price', 'inventory', 'order', 'categories', 'description', 'short_description')}),
        ('Shipping', {'fields': ('weight', 'weight_units'), 'classes': ('collapse',)}),
        ('Meta', {'fields': ('site', 'created', 'modified', 'total_sold',), 'classes': ('collapse',)}),
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

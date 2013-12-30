from django.contrib import admin

from shop.products.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'site', 'parent', 'order', 'active')
    list_filter = ('site',)
    search_fields = ('name', 'parent')
    prepopulated_fields = {'slug': ('name',)}
    exclude = ('site',)
    ordering = ('order',)

admin.site.register(Category, CategoryAdmin)

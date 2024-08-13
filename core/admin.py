from django.contrib import admin
from .models import Store, Product, SocialMedia, SocialMediaProduct, Category

class StoreAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'address', 'phone_number', 'email', 'logo_preview', 
        'mission', 'vision', 'strategic_objectives', 'organizational_culture', 
        'business_strategy', 'company_policies'
    )
    list_filter = ('name', 'address', 'email')
    search_fields = ('name', 'address', 'phone_number', 'email')
    fieldsets = (
        (None, {
            'fields': ('name', 'address', 'phone_number', 'email', 'logo', 'description')
        }),
        ('Company Details', {
            'classes': ('collapse',),
            'fields': (
                'mission', 'vision', 'strategic_objectives', 'organizational_culture',
                'business_strategy', 'company_policies'
            ),
        }),
    )
    
    def logo_preview(self, obj):
        if obj.logo:
            return f'<img src="{obj.logo.url}" width="100" height="100" />'
        return 'No image'
    logo_preview.allow_tags = True
    logo_preview.short_description = 'Logo Preview'

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description', 'price', 'store', 'image_preview', 'category_list'
    )
    list_filter = ('store', 'price', 'categories')
    search_fields = ('name', 'description', 'store__name', 'categories__name')
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'price', 'image', 'store', 'categories')
        }),
    )
    
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" height="100" />'
        return 'No image'
    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'
    
    def category_list(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    category_list.short_description = 'Categories'

class SocialMediaAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description', 'logo_preview', 'store', 'link'
    )
    list_filter = ('name',)
    search_fields = ('name', 'description', 'store__name', 'link')
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'logo', 'store', 'link')
        }),
    )
    
    def logo_preview(self, obj):
        if obj.logo:
            return f'<img src="{obj.logo.url}" width="100" height="100" />'
        return 'No image'
    logo_preview.allow_tags = True
    logo_preview.short_description = 'Logo Preview'

class SocialMediaProductAdmin(admin.ModelAdmin):
    list_display = (
        'link', 'product', 'social_media'
    )
    list_filter = ('product', 'social_media')
    search_fields = ('link', 'product__name', 'social_media__name')
    fieldsets = (
        (None, {
            'fields': ('link', 'product', 'social_media')
        }),
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
    )

admin.site.register(Store, StoreAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(SocialMediaProduct, SocialMediaProductAdmin)
admin.site.register(Category, CategoryAdmin)

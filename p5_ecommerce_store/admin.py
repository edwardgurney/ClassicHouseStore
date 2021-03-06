from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import (Product, Category, Bag, BagItem, ShippingAddress,
                     Rating, NewsLetterSubs)


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description')
    list_filter = ('artist', 'label', 'title')
    search_fields = ['title', 'artist']
    list_display = ('title', 'artist', 'slug', 'label', 'price')


# Register your models here.
admin.site.register(Category)
admin.site.register(Bag)
admin.site.register(BagItem)
admin.site.register(ShippingAddress)
admin.site.register(Rating)
admin.site.register(NewsLetterSubs)

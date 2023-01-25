from django.contrib import admin

# Register your models here.

from .models import products, review

admin.site.register(products)
admin.site.register(review)

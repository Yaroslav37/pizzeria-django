from django.contrib import admin
from products.models import ProductCategory, Product, NewsArticle, Review, FAQ

# Register your models here.

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(NewsArticle)
admin.site.register(Review)
admin.site.register(FAQ)

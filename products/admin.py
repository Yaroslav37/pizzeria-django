from django.contrib import admin
from products.models import ProductCategory, Product, NewsArticle, Review, FAQ, Banner, BannerSettings

# Register your models here.

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(NewsArticle)
admin.site.register(Review)
admin.site.register(FAQ)
admin.site.register(Banner)
admin.site.register(BannerSettings)

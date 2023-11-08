from django.db import models
from users.models import User

# Create your models here.


class NewsArticle(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    img = models.URLField(default='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Empty_set_symbol.svg/640px-Empty_set_symbol.svg.png')
    url = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    username = models.CharField(max_length=120, blank=True)
    grade = models.CharField(max_length=5, blank=True)
    text_review = models.CharField(max_length=2000)
    timestamp = models.DateTimeField(auto_now_add=True)


class FAQ(models.Model):
    term = models.CharField(max_length=100)
    definition = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created_timestamp = models.DateField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f"Корзина {self.user.email}, продукт - {self.product.name}"

    def sum(self):
        return self.product.price * self.quantity

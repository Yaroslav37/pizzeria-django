
from django.urls import path

from products.views import products, basket_add, basket_remove, about, news, review_send, review, term, contacts, promo, confidentiality, vacancies, test, test2, news_detail, test3

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('about', about, name='about'),
    path('news', news, name='news'),
    path('term', term, name='term'),
    path('contacts', contacts, name='contacts'),
    path('promo', promo, name='promo'),
    path('confidentiality', confidentiality, name='confidentiality'),
    path('vacancies', vacancies, name='vacancies'),
    path('test', test, name='test'),
    path('test2', test2, name='test2'),
    path('test3', test3, name='test3'),
    path('news_details/<title>', news_detail, name='news_details'),

    path('review_send', review_send, name='review_send'),
    path('review', review, name='review'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
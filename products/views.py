from django.shortcuts import render, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from products.models import Product, ProductCategory, Basket, NewsArticle, Review, FAQ
from django.contrib.auth.decorators import login_required
import requests
import random
from .forms import ProductSearchForm
from django.http import JsonResponse
from users.models import User

# Create your views here.

import logging

logger = logging.getLogger(__name__)


def my_view(request):
    logger.debug('Debug message')  # Пример логирования с уровнем DEBUG
    logger.info('Info message')    # Пример логирования с уровнем INFO
    logger.warning('Warning message')  # Пример логирования с уровнем WARNING
    logger.error('Error message')      # Пример логирования с уровнем ERROR
    logger.critical('Critical message')  # Пример логирования с уровнем CRITICAL


def index(request):
    context = {
        'title': 'main',
        'last_news': NewsArticle.objects.last()
    }
    return render(request, 'products/index.html', context)


def promo(request):
    context = {
        'title': 'promo',
    }
    return render(request, 'products/promo.html', context)


def vacancies(request):
    context = {
        'title': 'promo',
    }
    return render(request, 'products/vacancies.html', context)


def category(request):
    context = {
        'title': 'promo',
    }
    return render(request, 'products/vacancies.html', context)



def confidentiality(request):
    context = {
        'title': 'confidentiality',
    }
    return render(request, 'products/confidentiality.html', context)


def contacts(request):
    context = {
        'title': 'contacts',
    }
    return render(request, 'products/contacts.html', context)


def term(request):
    context = {
        'title': 'main',
        'terms': FAQ.objects.all(),
    }
    return render(request, 'products/faq.html', context)


def review(request):
    context = {
        'reviews': Review.objects.all()
    }
    return render(request, 'products/review.html', context)


def products(request):
    products_ = Product.objects.all()
    search_form = ProductSearchForm(request.GET)

    if search_form.is_valid():
        search_query = search_form.cleaned_data['search_query']
        products_ = products_.filter(name__icontains=search_query)

    context = {
        'title': 'products',
        'products': products_,
        'categories': ProductCategory.objects.all(),
        'search_form': search_form,
    }
    return render(request, 'products/products.html', context)


def about(request):
    context = {
        'title': 'about',
    }
    return render(request, 'products/about.html', context)


def test(request):
    context = {
        'title': 'test',
    }
    return render(request, 'products/test.html', context)


def test2(request):
    context = {
        'title': 'test2',
    }
    return render(request, 'products/test2.html', context)

def test3(request):
    context = {
        'title': 'test2',
    }
    return render(request, 'products/test3.html', context)

def news_detail(request, title):
    context = {
        'title': 'news_detail',
        'article': NewsArticle.objects.filter(title=title)
    }
    return render(request, 'products/full_article.html', context)


def news(request):
    url = 'https://newsapi.org/v2/everything?q=pizza&apiKey=20d95eef27454a9e990d505cb55f92cf'
    # pizza_news = requests.get(url).json()
    # i = random.randint(1, 100)
    # a = pizza_news['articles']
    # desc = []
    # title = []
    # img = []
    # news_url = []
    #
    # f = a[i]
    # title = f['title']
    # desc = f['description']
    # img = f['urlToImage']
    # news_url = f['url']
    #
    # existing_article = NewsArticle.objects.filter(title=title).first()
    # if existing_article:
    #     existing_article.description = desc
    #     existing_article.img = img
    #     existing_article.url = news_url
    #     existing_article.save()
    # else:
    #     new_article = NewsArticle(
    #         title=title,
    #         description=desc,
    #         img=img,
    #         url=news_url
    #     )
    #     new_article.save()

    context = {'news': NewsArticle.objects.all()}
    return render(request, 'products/news.html', context)

# @csrf_exempt
# def news_view(request):
#     # Вызываем представление get_news для получения новостей
#     news_data = get_news(request)
#
#     # Если есть статьи новостей, передаем их в шаблон
#     if 'articles' in news_data:
#         articles = news_data['articles']
#         return render(request, 'products/news.html', {'articles': articles})
#
#     # Если произошла ошибка, передаем ошибку в шаблон
#     elif 'error' in news_data:
#         error_message = news_data['error']
#         return render(request, 'products/news.html', {'error_message': error_message})
#
#     return render(request, 'products/news.html', {'error_message': 'Что-то пошло не так'})
#
#
#
# def get_news(request):
#     api_key = '20d95eef27454a9e990d505cb55f92cf'
#     api_url = f'https://newsapi.org/v2/everything?q=pizza&apiKey={api_key}'
#
#     try:
#         response = requests.get(api_url)
#         data = response.json()
#
#         if data.get('articles'):
#             articles = data['articles']
#             return JsonResponse({'articles': articles})
#
#     except Exception as e:
#         return JsonResponse({'error': str(e)})
#
#     return JsonResponse({'error': 'Не удалось получить новости'})
#
# @csrf_exempt
# def refresh_news(request):
#     # Вызываем представление get_news для получения новостей
#     news_data = get_news(request)
#
#     # Если есть статьи новостей, добавляем первую в базу данных
#     if 'articles' in news_data:
#         articles = news_data['articles']
#         if articles:
#             article_data = articles[0]
#             NewsArticle.objects.create(
#                 title=article_data['title'],
#                 description=article_data['description'],
#                 url=article_data['url']
#             )
#             return JsonResponse({'status': 'success'})
#
#     return JsonResponse({'error': 'Не удалось обновить новости'})

@login_required
def review_send(request):
    if request.method == 'POST':
        rating = request.POST['rating']
        review_text = request.POST['review-text']
        username = request.user.username

        review = Review(username=username, grade=rating, text_review=review_text)
        review.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])



@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
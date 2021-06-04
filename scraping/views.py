from django.shortcuts import render
from django.views import View
from .models import Product
from django.utils import timezone
import datetime as dt
from .scrapingAmazon import scraping
from .scrapingFlipkart import scrapingFlip
from .forms import SearchForm
from .utils import *

# Create your views here.

class ScrapingView(View):
    def get(self, request):
        if self.request.GET:
            self.form = SearchForm(self.request.GET)
        else:
            self.form = SearchForm()
        context = {}
        if self.form.is_valid():
            query_key = self.form.cleaned_data['query_key']
            print(query_key)
        
            saved_products = Product.objects.filter(name__icontains = query_key)
            
            if saved_products:
                if (timezone.now() - saved_products[0].updated_at).days <= THRESHOLD_TIME_OF_EXPIRATION:
                    for products in saved_products:
                        context[products.website_name] = products
                else:
                    amazon_product = scraping(searchKey=query_key)
                    context[WEBSITE_AMAZON] = amazon_product

                    flipkart_product = scrapingFlip(searchKey=query_key)
                    context[WEBSITE_FLIPKART] = flipkart_product


                    for product in saved_products:
                        if product.website_name == WEBSITE_AMAZON:
                            product.price = amazon_product.price
                            product.rating = amazon_product.rating

                        elif product.website_name == WEBSITE_FLIPKART:
                            product.price = flipkart_product.price
                            product.rating = flipkart_product.rating
                        
                    saved_products.update()

            else:
                amazon_product = scraping(searchKey=query_key)
                context[WEBSITE_AMAZON] = amazon_product
                amazon_product.save()

                flipkart_product = scrapingFlip(searchKey=query_key)
                context[WEBSITE_FLIPKART] = flipkart_product
                flipkart_product.save()

                

        context['form'] = self.form

        return render(request, 'scraping/home.html', context=context)

            

from django.shortcuts import render
from django.views import View
from .models import Product
from django.utils import timezone
import datetime as dt
from .forms import SearchForm

THRESHOLD_TIME_OF_EXPIRATION = 2
WEBSITE_AMAZON = 'amazon'
WEBSITE_FLIPKART = 'fliptkart'
WEBSITE_PICKABOO = 'pickaboo'
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
            # Here you will scrap from amazon, flipkart, pikaboo
            # Something will be called here
            # I will get those data from a dictionary
            # amazon_dict = scrap_ama(query_key)
            # flipkart_dict = scrap_flip(query_key)
            # dict = [
            #   product1, product2, product3
            # ]

            # product1 = Product.objects.create(
                # name = jfdajkdsf
            # )
            saved_products = Product.objects.filter(name = query_key) # will get 3 products
            
            if saved_products:
                if timezone.now() - saved_products[0].updated_at < THRESHOLD_TIME_OF_EXPIRATION:
                    for products in saved_products:
                        context[products.website_name] = products
            else:
                # please scrap here and return me 3 objects
                pass
        context['form'] = self.form

        return render(request, 'scraping/home.html', context)
            

            

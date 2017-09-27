from oscar.apps.catalogue.views import CatalogueView as TemplateView
from oscar.apps.catalogue.views import ProductDetailView as DetailView
from oscar.apps.catalogue.views import ProductCategoryView as TemplateCategoryView
from oscar.apps.catalogue.models import Product
from oscar.apps.partner.models import StockRecord

from django.utils.translation import ugettext_lazy as _
from django.utils.translation import LANGUAGE_SESSION_KEY

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django import template

# import urllib2, locale

def currency_conv_view(request):
    currency_code = request.GET['currency_code']
    factor = {}
    try: 
        req = urllib2.urlopen('http://finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1d1t1&s=INR'+currency_code+'=X') 
        result = req.read() 
        factor.update({currency_out:result.split(',')[1]}) 
    except:
        factor = {'INR':1.00, 'USD':0.0155, 'GBP':0.0115, 'EUR':0.0134}

    request.session['currency_code'] = currency_code 
    request.session['currency_factor'] = factor[currency_code]
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

#    currency_code = request.GET['currency_code']
#    factor = {}
#    factor = {'INR':1.00, 'USD':0.014, 'GBP':0.014, 'EUR':0.013}
#    request.session['currency_code'] = currency_code 
#    request.session['currency_factor'] = factor[currency_code]
#    return HttpResponseRedirect(request.META['HTTP_REFERER'])

class CatalogueView(TemplateView):
    """
    Browse all products in the catalogue
    """
    def get_context_data(self, **kwargs):
        ctx = {}
        ctx['summary'] = _("All products")
        search_context = self.search_handler.get_search_context_data(
            self.context_object_name)
        ctx.update(search_context)

        try:
            sorttype = self.request.GET['sort']
        except:
            sorttype = None

        try:
            price_min = self.request.GET['price_min']
            price_max = self.request.GET['price_max']
        except:
            price_min = price_max = None


        if sorttype == 'low-to-high':
            ctx['products'] = Product.objects.all().order_by('stockrecords__price_excl_tax')
        elif sorttype == 'high-to-low':
            ctx['products'] = Product.objects.all().order_by('-stockrecords__price_excl_tax')
        elif sorttype == 'ekaya-recommends':
            temp = []
            products = Product.objects.all()
            for product in products:
                if 'Ekaya Recommends: True' in product.attribute_summary:
                    temp.append(product)
            ctx['products'] = temp
        elif price_min:
            from decimal import Decimal as D
            price_min = D(price_min)
            price_max = D(price_max)
            stockrecords = StockRecord.objects.filter(price_excl_tax__gte=price_min, price_excl_tax__lte=price_max,)
            temp = []
            for stockrecord in stockrecords:
                temp.append(stockrecord.product)
            ctx['products'] = list(set(temp))
        else:   
            pass

        return ctx

class ProductCategoryView(TemplateCategoryView):
    def get_context_data(self, **kwargs):
        ctx = super(ProductCategoryView, self).get_context_data(**kwargs)
        ctx['category'] = self.category
        search_context = self.search_handler.get_search_context_data(
            self.context_object_name)
        ctx.update(search_context)

        dict_keys = self.request.GET.keys()
        if 'sort' in dict_keys:
            sorttype = self.request.GET['sort']
        else:
            sorttype = None

        if 'price_min' in dict_keys:
            price_min = self.request.GET['price_min']
            price_max = self.request.GET['price_max']
        else:
            price_min = price_max = None

        ctx = {}
        ctx['category'] = self.category
        ctx['summary'] = _("All products")
        search_context = self.search_handler.get_search_context_data(
            self.context_object_name)
        ctx.update(search_context)

        if sorttype == 'low-to-high':
            ctx['products'] = Product.objects.all().order_by('stockrecords__price_excl_tax')
        elif sorttype == 'high-to-low':
            ctx['products'] = Product.objects.all().order_by('-stockrecords__price_excl_tax')
        elif sorttype == 'ekaya-recommends':
            temp = []
            products = Product.objects.all()
            for product in products:
                if 'Ekaya Recommends: True' in product.attribute_summary:
                    temp.append(product)
            ctx['products'] = temp
        elif price_min:
            from decimal import Decimal as D
            price_min = D(price_min)
            price_max = D(price_max)
            stockrecords = StockRecord.objects.filter(price_excl_tax__gte=price_min, price_excl_tax__lte=price_max,)
            temp = []
            for stockrecord in stockrecords:
                temp.append(stockrecord.product)
            ctx['products'] = list(set(temp))            
        else:
            pass

        return ctx

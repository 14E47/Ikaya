from django.utils.translation import LANGUAGE_SESSION_KEY
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django import template

import urllib2, locale

def currency_conv_view(request):
    currency_code = request.GET['currency_code']
    factor = {}
    factor = {'INR':1.00, 'USD':0.015, 'GBP':0.011, 'EUR':0.014}
    request.session['currency_code'] = currency_code 
    request.session['currency_factor'] = factor[currency_code]
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
    # return HttpResponseRedirect('/')

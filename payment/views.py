from __future__ import unicode_literals
from django.shortcuts import render
import binascii
import datetime
import hashlib
import requests
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from pytz import timezone 
from oscar.apps.payment.models import Source
from decimal import Decimal as D
import logging, pdb

from django.views.generic import RedirectView, View
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.http import urlencode
from django.utils import six
from django.utils.translation import ugettext_lazy as _

import oscar
from oscar.apps.payment.exceptions import UnableToTakePayment
from oscar.core.exceptions import ModuleNotFoundError
from oscar.core.loading import get_class, get_model
from oscar.apps.shipping.methods import FixedPrice, NoShippingRequired

from urlparse import parse_qs, urlparse

from django.conf import settings
from django.template import loader,RequestContext
from django.shortcuts import render, render_to_response
## from markatix.partner.models import Partner, PartnerShop
#from payment_icici.models import IkayaPayment


# Load views dynamically
PaymentDetailsView = get_class('checkout.views', 'PaymentDetailsView')
CheckoutSessionMixin = get_class('checkout.session', 'CheckoutSessionMixin')

ShippingAddress = get_model('order', 'ShippingAddress')
Country = get_model('address', 'Country')
Basket = get_model('basket', 'Basket')
Repository = get_class('shipping.repository', 'Repository')
Selector = get_class('partner.strategy', 'Selector')
Source = get_model('payment', 'Source')
SourceType = get_model('payment', 'SourceType')
try:
    Applicator = get_class('offer.applicator', 'Applicator')
except ModuleNotFoundError:
    # fallback for django-oscar<=1.1
    Applicator = get_class('offer.utils', 'Applicator')

from oscar.core import prices
storeId = getattr(settings, "STORE_ID", None)
sharedSecret = getattr(settings, "SECRET_ID", None)
currency = getattr(settings, "CURRENCY", None)
# from .forms import MyModelForm
 
#disabling csrf (cross site request forgery)

def payment_icici(request):
    storeId = "3387000704"
    sharedSecret = "Et25zcXlXf"
    time = getDateTime()
    total = request.basket.total_incl_tax
    chargetotal = str(int(total))
    basket = request.basket.id
    print(chargetotal) 
    print(basket)
    currency = "356"
    string = (storeId + time + chargetotal + currency + sharedSecret)
    stringToHash = string.encode()
    ascii = binascii.b2a_hex(bytes(stringToHash))
    hash_object = hashlib.sha1(ascii)
    hex_dig = hash_object.hexdigest()
    print(hex_dig)
    return render(request, 'checkout/payment_details.html', {"sharedSecret":sharedSecret, "chargetotal":chargetotal,"storeId":storeId, "time":time,"hex_dig":hex_dig, "basket":basket })


def getDateTime():

    india = timezone('Asia/Kolkata')
    sa_time = datetime.now(india)
    now = sa_time.strftime("%Y:%m:%d-%H:%M:%S")
    print(now)
    return now

def success(request):
    reponse = request.GET.get('responseSuccessURL')
    print(reponse)
    
    return render(request,'response_success.html')    

def fail(request):
    reponse = request.GET.get('responseFailURL')
    print(reponse)
    
    return render(request,'response_fail.html') 


class SuccessResponseView(PaymentDetailsView):
    template_name = 'checkout/payment_details.html'
    template_name_preview = 'checkout/preview.html'
    preview = False

    @property
    def pre_conditions(self):
        return []

    def get(self, request, *args, **kwargs):
        """
        Fetch details about the successful transaction from PayPal.  We use
        these details to show a preview of the order with a 'submit' button to
        place it.
        """
        try:
            print request.GET
            # self.payer_id = request.GET['PayerID']
            # self.token = request.GET['token']
        except KeyError:
            # Manipulation - redirect to basket page with warning message
            logger.warning("Missing GET params on success response page")
            messages.error(
                self.request,
                _("Unable to determine PayPal transaction details"))
            return HttpResponseRedirect(reverse('basket:summary'))

        # Reload frozen basket which is specified in the URL
        kwargs['basket'] = self.load_frozen_basket(kwargs['basket_id'])
        if not kwargs['basket']:
            logger.warning(
                "Unable to load frozen basket with ID %s", kwargs['basket_id'])
            messages.error(
                self.request,
                _("No basket was found that corresponds to your "
                  "PayPal transaction"))
            return HttpResponseRedirect(reverse('basket:summary'))

        # logger.info(
        #     "Basket #%s - showing preview with payer ID %s and token %s",
        #     kwargs['basket'].id, self.payer_id, self.token)

        return super(SuccessResponseView, self).get(request, *args, **kwargs)

    def load_frozen_basket(self, basket_id):
        # Lookup the frozen basket that this txn corresponds to
        try:
            basket = Basket.objects.get(id=basket_id, status=Basket.FROZEN)
        except Basket.DoesNotExist:
            basket = Basket.objects.get(id=basket_id)
            # return None

        # Assign strategy to basket instance
        if Selector:
            basket.strategy = Selector().strategy(self.request)

        # Re-apply any offers
        Applicator().apply(request=self.request, basket=basket)

        return basket

    def get_context_data(self, **kwargs):
        ctx = super(SuccessResponseView, self).get_context_data(**kwargs)

        if not hasattr(self, 'payer_id'):
            return ctx
        return ctx

    def post(self, request, *args, **kwargs):
        """
        Place an order.

        We fetch the txn details again and then proceed with oscar's standard
        payment details view for placing the order.
        """
        error_msg = _(
            "A problem occurred communicating with CCAvenue "
            "- please try again later"
        )
        try:
            payment_id = request.POST['ipgTransactionId']
            amount = float(request.POST['chargetotal'])
            currency = request.basket.currency
            basket_id = request.basket.id
#            email = request.user.email
 #           razorpay_details = {'payment_id':payment_id, 'amount':amount, 'currency':currency, 
  #                  'email': request.user.email, 'contact': '7568373724'}

            if payment_id:
                pass
            else:
                messages.error(self.request, error_msg)
                return HttpResponseRedirect(reverse('basket:summary'))

        except KeyError:
            # Probably suspicious manipulation if we get here
            messages.error(self.request, error_msg)
            return HttpResponseRedirect(reverse('basket:summary'))

        # Reload frozen basket which is specified in the URL
        basket = self.load_frozen_basket(kwargs['basket_id'])
        order_number = self.generate_order_number(basket)
        self.checkout_session.set_order_number(order_number)

        if not basket:
            messages.error(self.request, error_msg)
            return HttpResponseRedirect(reverse('basket:summary'))

        submission = self.build_submission(basket=basket, context={'payment_id': payment_id, 'payment_amount': amount})
        return self.submit(**submission)

    def build_submission(self, **kwargs):
#        email = kwargs['context']['email']
        payment_id = kwargs['context']['payment_id']
        payment_amount = kwargs['context']['payment_amount']
        kwargs.pop('context')
        
        submission = super(
            SuccessResponseView, self).build_submission(**kwargs)

 #       submission['order_kwargs']['email'] = email
        submission['payment_kwargs']['payment_id'] = payment_id
        submission['payment_kwargs']['payment_amount'] = payment_amount    

        return submission

    def handle_payment(self, order_number, total, **kwargs):
        """
        Complete payment with Razorpay.
        """
        try:
            pass
        except PayPalError:
            raise UnableToTakePayment()
        # if not confirm_txn.is_successful:
        #     raise UnableToTakePayment()

        # Record payment source and event
        source_type, is_created = SourceType.objects.get_or_create(
            name='ICICI')
        source = Source(source_type=source_type,
                        currency=total.currency,
                        amount_allocated=kwargs['payment_amount'],
                        amount_debited=kwargs['payment_amount'])
        self.add_payment_source(source)
        self.add_payment_event('complete', kwargs['payment_amount'] ,
                               reference=kwargs['payment_id'])

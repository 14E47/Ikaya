from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt
from payment import views

urlpatterns = [
    url(r'^payment_page/$', views.payment_icici, name='payment_icici'),
    url(r'^place-order/(?P<basket_id>\d+)/$',
        csrf_exempt(views.SuccessResponseView.as_view()), name='razorpay-place-order'),
    url(r'^success/$', views.success, name='success'),
    url(r'^fail/$', views.fail, name='fail'),
    # url(r'^getdata/$', views.createHash, name='home'),
]
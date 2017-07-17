"""ikaya_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.views.generic.base import TemplateView
from django.contrib import admin

from django.conf.urls.static import static
from django.conf.urls import include, url
from django.conf import settings

from oscar.app import application

from custom_block import urls as custom_block_urls
from journal import urls as journal_urls

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about$', TemplateView.as_view(template_name='about.html'), name="about"),
    url(r'^journal1$', TemplateView.as_view(template_name='journal.html'), name="journal"),
    url(r'^contact$', TemplateView.as_view(template_name='contact.html'), name="contact"),
    url(r'^retailer$', TemplateView.as_view(template_name='retailer.html'), name="retailer"),
    url(r'^privacy$', TemplateView.as_view(template_name='privacy.html'), name="privacy"),
    url(r'^terms$', TemplateView.as_view(template_name='terms.html'), name="terms"),

    url(r'', include(application.urls)),
    url(r'^custom-image/', include(custom_block_urls)),
    url(r'^journal/', include(journal_urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
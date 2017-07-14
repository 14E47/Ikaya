from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from oscar.models.fields import ExtendedURLField

class CustomImage(models.Model):
    name = models.CharField(_("Name"), max_length=128, blank=True)
    link_url = models.URLField(
        _('Link URL'), blank=True,
        help_text=_('This is where this promotion links to'))
    image = models.ImageField(
        _('Image'), upload_to=settings.OSCAR_PROMOTION_FOLDER,
        max_length=255, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(_('Text'), blank=True)
    text_colour = models.CharField(_('Text Colour'), max_length=200, default='', blank=True) 
    button = models.CharField(_('Button Text'), max_length=200, default='', blank=True)

    def __str__(self):
        return self.name
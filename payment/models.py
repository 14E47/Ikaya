from __future__ import unicode_literals

from django.db import models

# Create your models here.
class IkayaPayment(models.Model):
	payment_id = models.CharField(max_length=100)
	basket_id = models.CharField(max_length=100, blank=True)
	amount = models.CharField(max_length=100)
	currency = models.CharField(max_length=100)

from decimal import Decimal as D
from django.template.loader import render_to_string

from oscar.apps.shipping import methods
from oscar.core import prices

from django.conf import settings
from ikaya_project import shipping_zone

class Standard(methods.Base):
    code = 'Standard'
    name = 'Shipping'

    charge_excl_tax = D('0.0')
    charge_incl_tax = D('0.0')

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=self.charge_excl_tax, incl_tax=self.charge_incl_tax)

class Standard_Zone_A(methods.Base):
    code = 'Standard_Zone_A'
    name = 'Shipping'

    charge_excl_tax = D(str(shipping_zone.ZONE_PRICING['A']))
    charge_incl_tax = D(str(shipping_zone.ZONE_PRICING['A']))

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=self.charge_excl_tax, incl_tax=self.charge_incl_tax)

class Standard_Zone_B(methods.Base):
    code = 'Standard_Zone_B'
    name = 'Shipping'

    charge_excl_tax = D(str(shipping_zone.ZONE_PRICING['B']))
    charge_incl_tax = D(str(shipping_zone.ZONE_PRICING['B']))

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=self.charge_excl_tax, incl_tax=self.charge_incl_tax)

class Standard_Zone_C(methods.Base):
    code = 'Standard_Zone_C'
    name = 'Shipping'

    charge_excl_tax = D(str(shipping_zone.ZONE_PRICING['C']))
    charge_incl_tax = D(str(shipping_zone.ZONE_PRICING['C']))

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=self.charge_excl_tax, incl_tax=self.charge_incl_tax)

class Standard_Zone_D(methods.Base):
    code = 'Standard_Zone_D'
    name = 'Shipping'

    charge_excl_tax = D(str(shipping_zone.ZONE_PRICING['D']))
    charge_incl_tax = D(str(shipping_zone.ZONE_PRICING['D']))

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=self.charge_excl_tax, incl_tax=self.charge_incl_tax)

class Standard_Zone_E(methods.Base):
    code = 'Standard_Zone_E'
    name = 'Shipping'

    charge_excl_tax = D(str(shipping_zone.ZONE_PRICING['E']))
    charge_incl_tax = D(str(shipping_zone.ZONE_PRICING['E']))

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=self.charge_excl_tax, incl_tax=self.charge_incl_tax)

class Standard_Zone_F(methods.Base):
    code = 'Standard_Zone_F'
    name = 'Shipping'

    charge_excl_tax = D(str(shipping_zone.ZONE_PRICING['F']))
    charge_incl_tax = D(str(shipping_zone.ZONE_PRICING['F']))

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=self.charge_excl_tax, incl_tax=self.charge_incl_tax)

class Standard_Zone_G(methods.Base):
    code = 'Standard_Zone_G'
    name = 'Shipping'

    charge_excl_tax = D(str(shipping_zone.ZONE_PRICING['G']))
    charge_incl_tax = D(str(shipping_zone.ZONE_PRICING['G']))

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=self.charge_excl_tax, incl_tax=self.charge_incl_tax)

class Standard_Zone_H(methods.Base):
    code = 'Standard_Zone_H'
    name = 'Shipping'

    charge_excl_tax = D(str(shipping_zone.ZONE_PRICING['H']))
    charge_incl_tax = D(str(shipping_zone.ZONE_PRICING['H']))

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=self.charge_excl_tax, incl_tax=self.charge_incl_tax)

class Standard_Zone_I(methods.Base):
    code = 'Standard_Zone_I'
    name = 'Shipping'

    charge_excl_tax = D(str(shipping_zone.ZONE_PRICING['I']))
    charge_incl_tax = D(str(shipping_zone.ZONE_PRICING['I']))

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=self.charge_excl_tax, incl_tax=self.charge_incl_tax)

class Standard_Zone_J(methods.Base):
    code = 'Standard_Zone_J'
    name = 'Shipping'

    charge_excl_tax = D(str(shipping_zone.ZONE_PRICING['J']))
    charge_incl_tax = D(str(shipping_zone.ZONE_PRICING['J']))

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=self.charge_excl_tax, incl_tax=self.charge_incl_tax)


class Standard_Zone_K(methods.Base):
    code = 'Standard_Zone_K'
    name = 'Shipping'

    charge_excl_tax = D(str(shipping_zone.ZONE_PRICING['K']))
    charge_incl_tax = D(str(shipping_zone.ZONE_PRICING['K']))

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=self.charge_excl_tax, incl_tax=self.charge_incl_tax)

class Standard_Zone_L(methods.Base):
    code = 'Standard_Zone_L'
    name = 'Shipping'

    charge_excl_tax = D(str(shipping_zone.ZONE_PRICING['L']))
    charge_incl_tax = D(str(shipping_zone.ZONE_PRICING['L']))

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=self.charge_excl_tax, incl_tax=self.charge_incl_tax)

class Standard_Zone_M(methods.Base):
    code = 'Standard_Zone_M'
    name = 'Shipping'

    charge_excl_tax = D(str(shipping_zone.ZONE_PRICING['M']))
    charge_incl_tax = D(str(shipping_zone.ZONE_PRICING['M']))

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=self.charge_excl_tax, incl_tax=self.charge_incl_tax)                    
from oscar.apps.shipping import repository

from . import methods
from decimal import Decimal as D

from django.conf import settings
from ikaya_project import shipping_zone

SHIPPING_TO_ZONE_MAPPING = {
    'A': methods.Standard_Zone_A(),
    'B': methods.Standard_Zone_B(),
    'C': methods.Standard_Zone_C(),
    'D': methods.Standard_Zone_D(),
    'E': methods.Standard_Zone_E(),
    'F': methods.Standard_Zone_F(),
    'G': methods.Standard_Zone_G(),
    'H': methods.Standard_Zone_H(),
    'I': methods.Standard_Zone_I(),
    'J': methods.Standard_Zone_J(),
    'K': methods.Standard_Zone_K(),
    'L': methods.Standard_Zone_L(),
    'M': methods.Standard_Zone_M(),
}

# Override shipping repository in order to provide our own two
# custom methods
class Repository(repository.Repository):
    def get_available_shipping_methods(
            self, basket, user=None, shipping_addr=None,
            request=None, **kwargs):
        overseas_free_shipping_limit = shipping_zone.FREE_SHIPPING_OTHERS_AMOUNT
        if basket.total_excl_tax > D(overseas_free_shipping_limit) or basket.total_incl_tax > D(overseas_free_shipping_limit):
            methods_f = (methods.Standard(),)

        elif shipping_addr:

            if shipping_addr.country.code == 'IN':
                methods_f = (methods.Standard(),)

            else:
                shipping_addr_country = shipping_addr.country.printable_name
                country_name_list = shipping_zone.ZONES.keys()
                methods_f = (methods.Standard(),)

                if shipping_addr_country in country_name_list:
                    shipping_addr_country_zone = shipping_zone.ZONES[shipping_addr_country]
                    methods_f = (SHIPPING_TO_ZONE_MAPPING[shipping_addr_country_zone],)

        else:
            methods_f = (methods.Standard(),)

        return methods_f
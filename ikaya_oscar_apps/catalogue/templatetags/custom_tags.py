from oscar.core.loading import get_model

from django.utils import timezone
from django import template

import pdb

register = template.Library()

category = get_model('catalogue', 'Category')
product_type = get_model('catalogue', 'ProductClass')
attribute_option_group = get_model('catalogue', 'AttributeOptionGroup')
attribute_option = get_model('catalogue', 'AttributeOption')
product_attribute = get_model('catalogue', 'ProductAttribute')
product_attribute_value = get_model('catalogue', 'ProductAttributeValue')

@register.assignment_tag(name='get_categories')
def get_categories():
    categories = category.get_tree()
    return categories

@register.assignment_tag(name='get_product_type')
def get_product_type():
    product_types = product_type.objects.all()
    return product_types    

@register.assignment_tag(name='get_prodcuct_type_attributes')
def get_prodcuct_type_attributes(product_type_obj):
    prodcuct_type_attributes = product_type_obj.attributes.all()
    return prodcuct_type_attributes

@register.assignment_tag(name='get_attribute_options')
def get_attribute_options(attribute_obj):
    attribute_options = []
    if attribute_obj.is_option:
        attribute_options = attribute_obj.option_group.options.all()
    return attribute_options 

@register.filter(name='get_product_attrib_array')
def get_product_attrib_array(product_obj):
    if product_obj.is_parent:
        variants = product_obj.children.all()
        attrib_value_list = []
        for item in variants:
            attribute_obj_list = item.attribute_values.all()
            for attrib in attribute_obj_list:
                attrib_value_list.append(attrib.value.option)

        attribute_obj_list = product_obj.attribute_values.all()
        for attrib in attribute_obj_list:
            attrib_value_list.append(attrib.value.option)

        attrib_value_list = list(set(attrib_value_list))
        attrib_value = ' '.join(attrib_value_list)
    else:
        attrib_value_list = []
        attribute_obj_list = product_obj.attribute_values.all()
        for attrib in attribute_obj_list:
            attrib_value_list.append(attrib.value.option)
        attrib_value_list = list(set(attrib_value_list))
        attrib_value = ' '.join(attrib_value_list)
    return attrib_value.lower()

    # <-- above template tag usage in *.html file -->
    # {% get_categories as categories %}
    # {% for category in categories %}
    #     {{category.name}}<br>
    # {% endfor %}

    # <br><br>
    # {% get_product_type as product_types %}
    # {% for product_type in product_types %}
    #     {{product_type.name}}<br>
    #     {% get_prodcuct_type_attributes product_type as attributes %}
    #     {% for attibute in attributes %} 
    #         {{attibute.name}}<br>
    #         {% get_attribute_options attibute as options %}
    #         {% for option in options %} 
    #             {{option.option}}<br>
    #         {% endfor %}
    #     {% endfor %}
    # {% endfor %}    
    # <-- above template tag usage in *.html file end -->

from oscar.apps.catalogue.models import Product

from custom_block.models import CustomImage

@register.assignment_tag(name='get_home_sections')
def get_home_sections(section):
    custom_image_section = CustomImage.objects.filter(name=section)
    if custom_image_section:
        custom_image_section = CustomImage.objects.get(name=section)
    return custom_image_section

@register.assignment_tag
def top_products():
	top_products = Product.objects.filter(parent__isnull=True)[:6]
	return top_products
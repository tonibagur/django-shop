# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from shop.models_bases import BaseOrder
from shop.models_bases.managers import OrderManager
from myproject.addressmodel import Address
from django.db import models

class Order(BaseOrder):
    objects = OrderManager()

    shipping_address = models.ForeignKey(Address, verbose_name=_('Dirección de envío'), blank=True, null=True, related_name='shipping_address')
    billing_address = models.ForeignKey(Address, verbose_name=_('Dirección de facturación'), blank=True, null=True, related_name='billing_address')

    def set_billing_address(self, billing_address):
        super(Order, self).set_billing_address(billing_address)
        self.billing_address = billing_address
        self.save()

    def set_shipping_address(self, shipping_address):
        super(Order, self).set_shipping_address(shipping_address)
        self.shipping_address = shipping_address
        self.save()

    class Meta(object):
        abstract = False
        app_label = 'shop'
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Brand(models.Model):
    brand_name = models.CharField(max_length=40)
    brand_desc = models.TextField(blank=True, null=True)

    class Meta(object):
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return self.brand_name



class Variant(models.Model):
    variant_name = models.CharField(max_length=40)
    variant_desc = models.TextField(blank=True, null=True)

    class Meta(object):
        verbose_name = _("Variant")
        verbose_name_plural = _("Variants")

    def __str__(self):
        return self.variant_name

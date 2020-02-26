from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Product(models.Model):
    prodName    = models.CharField(max_length=100, verbose_name=_("Product"))
    prodName    = models.TextField(verbose_name=_("Product Description"))
    prodPrice   = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Price"))
    prodCost    = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Cost"))
    prodCreated = models.DateTimeField(verbose_name=_("Created at"))
    """
    because Product model is a Class each product is an object(instance)
    so we need to define __str__ function to show he name of each product
    """
    def __str__(self):
        return self.prodName

class ProductImage(object):
    # Every product has an image. delete image if product deleted
    PIProduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))
    PIImage = models.ImageField(upload_to='product/', verbose_name=_("Image"))
    def __str__(self):
        return str(self.PIProduct)

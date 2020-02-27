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
    so we need to define __str__ function to show the name of each product
    """
    def __str__(self):
        return self.prodName

class ProductImage(models.Model):
    # Every product has an image. delete image if product deleted
    PIProduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))
    PIImage = models.ImageField(upload_to='product/', verbose_name=_("Image"))
    def __str__(self):
        return str(self.PIProduct)

class Category(models.Model):
    CATName = models.CharField(max_length=50)
    """
    Main category & sub category are same so Parent references to itself. if there's no sub cate
    it will be null
    """
    CATParent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    CATDesc = models.TextField()
    CATImg = models.ImageField(upload_to='category/')
    def __str__(self):
        return str(self.CATName)

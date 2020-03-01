from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

# Create your models here.
class Product(models.Model):
    prodName    = models.CharField(max_length=100, verbose_name=_("Product"))
    """
    - class Category is below, so we have to put it inside single quotes
    - Each product have a category
    - to avoid cross import erro we use 'appName.modelName' trick
    """
    prodCategory    = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    prodBrand       = models.ForeignKey('settings.Brand', on_delete=models.CASCADE, blank=True, null=True)
    prodDesc        = models.TextField(verbose_name=_("Product Description"))
    prodImage       = models.ImageField(upload_to='product/', verbose_name=_("Image"), blank=True, null=True)
    prodPrice       = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Price"))
    prodCost        = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Cost"))
    prodCreated     = models.DateTimeField(verbose_name=_("Created at"))
    prodSlug        = models.SlugField(blank=True, null=True)

    """
    because Product model is a Class each producSt is an object(instance)
    so we need to define __str__ function to show the name of each product
    """
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    """
    Override save method
    """
    def save(self, *args, **kwargs):
        # if there is no slug
        if not self.prodSlug :
            # Generate a slug from product name
            self.prodSlug = slugify(self.prodName)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.prodName)

class ProductImage(models.Model):
    # Every product has an image. delete image if product deleted
    PIProduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))
    PIImage = models.ImageField(upload_to='product/', verbose_name=_("Image"))

    def __str__(self):
        return str(self.PIProduct)

class Category(models.Model):
    CATName = models.CharField(max_length=50, verbose_name=_("Name"))
    """
    - Main category & sub category are same so Parent references to itself(Recursive relation).
    - if there's no sub category it will be null
    - Subcateogries are two levels down so a subcateogry can't have another subcateogry
    - [limit_choices_to]: show only parent categories (its parent is null)
    """
    CATParent = models.ForeignKey('self', on_delete=models.CASCADE, limit_choices_to={'CATParent__isnull': True}, verbose_name=_("Main Category"), blank=True, null=True)
    CATDesc = models.TextField(verbose_name=_("Description"))
    CATImg = models.ImageField(upload_to='category/', verbose_name=_("Image"))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return str(self.CATName)

class Product_Alternative(models.Model):
    """
    - Since both PAName & PAAlternative are related to the same model
    Django will see them as one, so we have to give them a related_name.
    """
    PAName = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='main_product', verbose_name=_("Product"))
    PAAlternative = models.ManyToManyField(Product, related_name='alternative_products', verbose_name=_("Alternatives"))

    class Meta:
        verbose_name = _("Product Alternative")
        verbose_name_plural = _("Product Alternatives")

    def __str__(self):
        return str(self.PAName)

class Product_Accessory(models.Model):
    """
    - Since both PAName & PAAlternative are related to the same model
    Django will see them as one, so we have to give them a related_name.
    """
    PACCName = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='main_accessory_product', verbose_name=_("Product"))
    PACCAlternative = models.ManyToManyField(Product, related_name='accessories_products', verbose_name=_("Accessories"))

    class Meta:
        verbose_name = _("Product Accessory")
        verbose_name_plural = _("Product Accessories")

    def __str__(self):
        return str(self.PACCName)

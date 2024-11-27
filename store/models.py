from django.db import models
from tinymce import models as tinymodels
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save


# Create your models here.
class Category(models.Model):
    name = models.CharField(_("Nombre categoria"), max_length=50)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return f'{self.pk} - {self.name}'
    


class Product(models.Model):
    name = models.CharField(_("Nombre"), max_length=200)
    description = tinymodels.HTMLField(_('Descripcion'))
    category = models.ManyToManyField(Category, verbose_name=_("Categorias"))
    stock = models.IntegerField(_("Stock"), default=0)

    def __str__(self):
        return f'{self.pk} - {self.name}'
    


class ProductImage(models.Model):
    product = models.ForeignKey(Product, verbose_name=_(""), on_delete=models.CASCADE)
    image = models.ImageField(_("Imagen"), upload_to='products/') 


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name=_("Usuario"), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_("Producto"), on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(_("Cantidad"))


"""
@receiver(pre_save, sender=Order)
def order_pre_save_receiver(sender, instance, **kwargs):
    if instance.product.stock < 0:
        pass
"""



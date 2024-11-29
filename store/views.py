from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .models import Product
from .forms import OrderForm

# Create your views here.
class HomeView(TemplateView):
    template_name = "store/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_list"] = Product.objects.all()[:6]
        return context
    

class ProductDetailView(DetailView):
    model = Product
    template_name = "store/product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order_form"] = OrderForm
        return context
    

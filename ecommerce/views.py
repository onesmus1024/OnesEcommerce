from django.shortcuts import render
from django.views import generic
from .models import User,Product
from .forms import SignUpForm,AddProduct
# Create your views here.

class SignUp(generic.CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'ecommerce/signup.html'
    success_url='../home'

    def get_initial(self):
        initial = super().get_initial()
        initial['username'] = 'enter your name'
        return initial


class Home(generic.TemplateView):
    template_name = 'ecommerce/home.html'


class ProductsView(generic.TemplateView):
    model= Product
    template_name = 'ecommerce/products.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products']= Product.objects.all()

        return context
class AddProductView(generic.CreateView):
    model = Product
    template_name='ecommerce/addproduct.html'
    form_class = AddProduct
    success_url='../products'
from django.shortcuts import render,redirect
from django.views import generic
from .models import User,Product
from .forms import SignUpForm,AddProduct
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def userlogout(request):
    logout(request)
def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        print("in register function")
        if form.is_valid:
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            form.save()
            user = authenticate(request,username=username,password=password)
            login(request,user=user)
            return redirect('home')
    else:
            form = UserCreationForm()
    context = {'form':form}
    return render(request=request,template_name="registration/register.html",context=context)

class SignUp(generic.CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'ecommerce/signup.html'
    success_url='../home'

    def get_initial(self):
        initial = super().get_initial()
        #initial['username'] = 'enter your name'
        return initial


class Home(generic.TemplateView):
    template_name = 'ecommerce/home.html'


class ProductsView(generic.TemplateView):
    model= Product
    template_name = 'ecommerce/products.html'
    #getting model data 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products']= Product.objects.all()

        return context
class AddProductView(generic.CreateView):
    model = Product
    template_name='ecommerce/addproduct.html'
    form_class = AddProduct
    success_url='../products'





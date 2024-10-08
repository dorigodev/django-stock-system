from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from apps.stock.models import Product
from apps.stock.forms import ProductForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You are not logged in!')
        return redirect('login_user')
    products = Product.objects.filter(disponibility=True).filter(store=request.user)
    return render(request, 'stock/index.html', {'products': products})

@login_required
def create_product(request):
    Form = ProductForm()
    if not request.user.is_authenticated:
        messages.error(request, 'You are not logged in!')
        return redirect('login')
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.store = request.user
            form.save()
            messages.success(request, 'Product successfully created')
            return redirect('index')
    return render(request, 'stock/create_product.html', {'form':Form})

def update_product(request, product_id):
    pass

def delete_product(request, product_id):
    pass

def search_product(request):
    pass
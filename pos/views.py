# pos/views.py
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import CreatUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register(request):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            form = CreatUserForm()
            if request.method == 'POST':
                form = CreatUserForm(request.POST)
                if form.is_valid():
                    form.save()
                    user = form.cleaned_data.get('username')
                    messages.success(request, 'Account was created created for ' + user)

                    return redirect('login')
        
        context = {'form' : form}
        return render(request, 'pos/register.html', context)

def loginPage(request):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('home')
                
                else:
                    messages.info(request, 'Username or Password is incorrect.')

        context = {}
        return render(request, 'pos/login.html', context)

def index(request):
    context = {}
    return render(request, 'pos/index.html', context)
    

def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


@login_required(login_url='login')
def product_list(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

@login_required(login_url='login')
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})



@login_required(login_url='login')
def add_to_cart(request, product_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        product = Product.objects.get(id=product_id)
        cart = request.session.get('cart', {})

        if product_id in cart:
            cart[product_id]['quantity'] += quantity
        else:
            cart[product_id] = {'name': product.name, 'price': product.price, 'quantity': quantity}

        request.session['cart'] = cart
        return redirect('product_list')


@login_required(login_url='login')
def cart_view(request):
    cart_items = request.session.get('cart', {}).values()
    total_amount = calculate_cart_total(request)

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_amount': total_amount})
    

@login_required(login_url='login')
def calculate_cart_total(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    return total

@login_required(login_url='login')
def checkout(request):
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        
        return redirect('payment_success')
    return render(request, 'pos/checkout.html')


@login_required(login_url='login')
def payment_success(request,):

    request.session['cart'] = {}
    
    return render(request, 'pos/payment_success.html', {
    })

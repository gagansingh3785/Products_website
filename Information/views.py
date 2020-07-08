from django.shortcuts import render, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, Http404
from .form import CreateUserForm, UserInformation, UpdateInfo
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Cart, Info, Order, Product, Tags
from django.contrib.auth.decorators import login_required
from .decorators import *


@if_logged_in
def login_page(request):
    print(request.META['HTTP_ACCEPT'])
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Incorrect credentials')
        else:
            login(request, user)
            info = Info.objects.get(user=user)
            if info.type_of_user == 'Buyer':
                return HttpResponseRedirect('homeB')
            elif info.type_of_user == 'Seller':
                return HttpResponseRedirect('homeS')
    return render(request, 'Information/login.html', {})


@if_logged_in
def register_page(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            messages.success(request, 'You are all set')
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('information'))
        else:
            for user in User.objects.all():
                if form.cleaned_data['email'] == user.email:
                    messages.error(request, 'Email already taken')
                    return render(request, 'Information/register.html', {'form': form})
            messages.error(request, 'Incorrect password format')
    return render(request, 'Information/register.html', {"form": form})


@login_required(login_url='login')
def user_information(request):
    form = UserInformation()
    print(request.method)
    if request.method == 'POST':
        print('inside')
        form = UserInformation(request.POST)
        if form.is_valid():
            info = Info()
            info.user = request.user
            info.phone = form.cleaned_data['phone']
            info.type_of_user = form.cleaned_data['type_of_user']
            info.save()
            logout(request)
            return HttpResponseRedirect(reverse('login'))
    return render(request, 'Information/user_info.html', {'form': form})


@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


@login_required(login_url='login')
def homeB(request):
    info = Info.objects.get(user=request.user)
    return render(request, 'Information/buyer_home.html', {'info': info,
                                                           'Clothing': 'Clothing',
                                                           'Footwear': 'Footwear',
                                                           'Electronics': 'Electronics',
                                                           'Books': 'Books',
                                                           'other': 'other'})


@login_required(login_url='login')
def homeS(request):
    info = Info.objects.get(user=request.user)
    products = Product.objects.filter(seller=info)
    return render(request, 'Information/seller_home.html', {'info': info, 'products': products})


@login_required(login_url='login')
def profileB(request):
    info = Info.objects.get(user=request.user)
    info = request.user.info
    print(info.order_set.all())
    orders = info.order_set.all()
    return render(request, 'Information/profileB.html', {'info': info, 'orders': orders})


@login_required(login_url='login')
def profileS(request):
    info = Info.objects.get(user=request.user)
    info = request.user.info
    print(info.order_set.all())
    orders = []
    products = Product.objects.filter(seller=info)
    for order in Order.objects.all():
        if order.product in products:
            orders.append(order)
    return render(request, 'Information/profileS.html', {'info': info, 'orders': orders})


@login_required(login_url='login')
def cancel_order(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return HttpResponseRedirect(reverse('profileB'))


@login_required(login_url='login')
def update(request):
    info = Info.objects.get(user=request.user)
    form = UpdateInfo()
    form.username = request.user.username
    if request.method == "POST":
        form = UpdateInfo(request.POST)
        if form.is_valid():
            user = request.user
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            info = Info.objects.get(user=request.user)
            info.address = form.cleaned_data['address']
            info.phone = form.cleaned_data['phone']
            info.save()
            user.save()
            return HttpResponseRedirect(reverse('profileB'))
    return render(request, 'Information/update_info.html', {'form': form, 'info': info})


@login_required(login_url='login')
def shop(request, category):
    info = Info.objects.get(user=request.user)
    products = Product.objects.filter(category=category)
    if request.method == "POST":
        products = []
        try:
            tag = Tags.objects.get(tag_name=request.POST['tag'])
            print(tag)
            for product in Product.objects.all():
                if product.category == category:
                    print(product.tags.all())
                    if tag in product.tags.all():
                        products.append(product)
                    print(products)
        except:
            print('tags do not exist')
        return render(request, 'Information/shop.html', {'info': info, 'products': products})
    return render(request, 'Information/shop.html', {'info': info, 'products': products})


@login_required(login_url='login')
def place_order(request, pk):
    product = Product.objects.get(id=pk)
    info = Info.objects.get(user=request.user)
    if request.method == "POST":
        order = Order()
        order.user_info = info
        order.product = product
        order.Delivery_address = request.POST['address']
        order.quantity = request.POST['quantity']
        order.status = 'Pending'
        order.save()
        return order_success(request, order.pk)
    return render(request, 'Information/confirm_buy.html', {'product': product, 'info': info})


@login_required(login_url='login')
def order_success(request, pk):
    order = Order.objects.get(id=pk)
    return render(request, 'Information/success.html', {'order': order})


@login_required(login_url='login')
def add_product(request):
    info = Info.objects.get(user=request.user)
    if request.method == "POST":
        product = Product()
        tag = Tags()
        tag.tag_name = request.POST.get('tag', request.POST['name'])
        tag.save()
        product.tags.add(tag)
        product.seller = info
        product.name = request.POST['name']
        product.category = request.POST['category']
        product.description = request.POST['description']
        product.product_image1 = request.FILES.get('image1','default.jpg')
        product.product_image2 = request.FILES.get('image2','default.jpg')
        product.product_image3 = request.FILES.get('image3','default.jpg')
        product.product_image4 = request.FILES.get('image4','default.jpg')
        product.price = request.POST['price']
        product.save()
        return HttpResponseRedirect(reverse('homeS'))
    return render(request, 'Information/add_product.html', {'info': info})


@login_required(login_url='login')
def edit_product(request, pk):
    info = Info.objects.get(user=request.user)
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.description = request.POST['description']
        product.category = request.POST['category']
        print(product.tags)
        tag = Tags()
        tag.tag_name = request.POST['tag']
        tag.save()
        product.tags.add(tag)
        product.product_image1 = request.FILES.get('image1', product.product_image1)
        product.product_image4 = request.FILES.get('image4', product.product_image4)
        product.product_image3 = request.FILES.get('image3', product.product_image3)
        product.product_image2 = request.FILES.get('image2', product.product_image2)
        product.save()
        return HttpResponseRedirect(reverse('homeS'))
    return render(request, 'Information/edit_product.html', {'product': product , 'info': info})

@login_required(login_url='login')
def remove(request, pk):
    info = Info.objects.get(user=request.user)
    if request.method == "POST":
        if request.POST['choice'] == 'yes':
            product = Product.objects.get(id=pk)
            product.delete()
        return HttpResponseRedirect(reverse('homeS'))
    return render(request, 'Information/remove.html', {'info': info})


@login_required(login_url='login')
def add_cart(request, pk):
    print('inside add_cart')
    if request.method == "GET":
        print('inside if')
        cart_add = Cart()
        cart_add.product = Product.objects.get(id=pk)
        cart_add.user_info = Info.objects.get(user=request.user)
        cart_add.save()
        return HttpResponse('Added to cart')
    return HttpResponse('Not added to cart')


@login_required(login_url='login')
def cart(request):
    info = Info.objects.get(user=request.user)
    cart_products = Cart.objects.filter(user_info=info)
    return render(request, 'Information/cart.html', {'orders': cart_products, 'info':info})

@login_required(login_url='login')
def remove_cart(request, pk):
    print(pk)
    item = Cart.objects.get(id=pk)
    item.delete()
    return HttpResponseRedirect(reverse('Cart'))

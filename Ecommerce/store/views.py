from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
import json

from django.urls import reverse

from .forms import ServiceForm
from .models import CommenttForm
import datetime
from .models import *

def store(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
	# Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
		cartItems = order['get_cart_items']
	products = Product.objects.all()
	context = {'products': products, 'cartItems': cartItems}
	return render(request, 'store/store.html',context)

def cart(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		# Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total': 0, 'get_cart_items': 0 }
		cartItems = order['get_cart_items']

	context = {'items':items,'order':order, 'cartItems': cartItems ,}
	return render(request, 'store/cart.html', context)



def cheekout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items

	else:
		# Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
		cartItems = order['get_cart_items']


	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cheekout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)
	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)
	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()
	return JsonResponse('item was added' ,safe=False)

def bikeview(request):
	return render(request,'store/view.html')




def ServiceBike(request):
	if request.method == "POST":
		form=ServiceForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,"your data are saved")
			return redirect(bikeview)


	else:
		form = ServiceForm()
		ser=service.objects.all()

		context={
			'ser':ser,
			'form':form,

		}
		return render(request,'store/serice.html',context)


def buy_parts(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		part = Buy_parts.objects.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
		cartItems = order['get_cart_items']

	context={
		'part':part,
		'items': items, 'order': order, 'cartItems': cartItems,
	}
	return render(request,'store/parts.html',context)

def register(request):
	if request.method == "POST":
		method_dict = request.POST.copy()
		first_name = method_dict.get('first_name')
		last_name = method_dict.get('last_name')
		username = method_dict.get('username')
		email = method_dict.get('email')
		password = method_dict.get('password')
		password2 = method_dict.get('password2')

		if password == password2:
			if User.objects.filter(username=username).exists():
				messages.error(request, 'Username already exist!')
			else:
				if User.objects.filter(email=email).exists():
					messages.error(request, 'Email already taken!')
				else:
					User.objects.create_user(username=username,
											 password=password,
											 first_name=first_name,
											 last_name=last_name,
											 email=email
											 )
					messages.success(request, 'You are successfully registered!')
					return HttpResponseRedirect(reverse('register'))
		else:
			messages.error(request, 'Password does not match!')

		return HttpResponseRedirect(reverse('register'))

	return render(request,'profile/Registration.html')

def login(request):
    if request.method == "POST":
        method_dict = request.POST.copy()
        username = method_dict.get('username')
        password = method_dict.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are successfully logged in!')
            # return HttpResponseRedirect(reverse('index'))
            return HttpResponseRedirect(reverse('bikeview'))
        else:
            messages.error(request, 'Invalid Credentials!')
            return HttpResponseRedirect(reverse('login'))

    return render(request, 'profile/login.html')

#
# def blog(request):
# 	faq = FAQ.objects.filter(status=True).order_by('created_at')
# 	context={
# 		'faq':faq,
# 	}
# 	return render(request,'store/blog.html',context)
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
	    return self.name

	# @property
	#
	#
	# def imageURL(self):
	# 	try:
	# 		url = self.image.url
	# 	except:
	# 		url = ''
	# 	return url


class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address

class service(models.Model):
	STATUS = (
		("engin", "engin"),
		("wash", "wash"),
		("glass", "glass"),
		("breakplate", "breakplate"),
	)
	BIKE = (
		("R15", "R15"),
		("Hero", "Hero"),
		("yamma", "yamma"),
	)


	user=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	phone=models.CharField(max_length=250)
	type=models.CharField(choices=STATUS, max_length=200)
	bike_type=models.CharField( choices=BIKE,max_length=250)
	list_date = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.phone


class Buy_parts(models.Model):
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	title=models.CharField(max_length=250)
	price=models.FloatField(max_length=4)
	image = models.ImageField(null=True, blank=True)

	def  __str__(self):
		return self.title

class Review(models.Model):

    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),

    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    comment = models.CharField(max_length=500, blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=40, choices=STATUS, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class CommenttForm(ModelForm):

	class Meta:
		model = Review
		fields = ['title', 'comment', 'rate']



class FAQ(models.Model):
    STATUS = (
        ("True", "True"),
        ("False", "False")
    )
    ordernumber = models.IntegerField()
    question = models.CharField(max_length=200)
    answer = models.TextField()
    status = models.CharField(choices=STATUS, max_length=200, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


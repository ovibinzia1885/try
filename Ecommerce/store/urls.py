from django.urls import path

from . import views


urlpatterns = [

	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('cheekout/', views.cheekout, name="cheekout"),
	path('update_Item/', views.updateItem, name="update_Item"),
	path('bikeview/', views.bikeview, name="bikeview"),
	path('ServiceBike/', views.ServiceBike, name="ServiceBike"),
	path('buy_parts/', views.buy_parts, name="buy_parts"),
	path('register/', views.register, name="register"),
	path('login/', views.login, name="login"),
	# path('blog/', views.blog, name="blog"),




]

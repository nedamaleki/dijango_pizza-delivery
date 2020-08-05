from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import PizzaModel

def adminloginpageview(request):
	return render(request,'adminloginpage.html',{})

def authenticateadmin (request):
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username = username, password = password)

	# user exists
	if user is not None and user.username=="admin":
		login (request, user)
		return redirect('adminhomepage')


	# user dose not exist
	if user is None:
		messages.add_message (request, messages.ERROR, "Invalid Credentials")
		return redirect ('adminloginpage')

def adminhomepageview(request):

	context={'pizzas':PizzaModel.objects.all()}
	return render (request, 'adminhomepage.html', context)

def adminlogout(request):
	logout(request)
	return redirect('adminloginpage')

def addpizza(request):
	name=request.POST['pizza']
	price=request.POST['price']
	PizzaModel(name=name, price=price).save()

	return redirect('adminhomepage')

def deletepizza(request, pizza_id):
	pizza = PizzaModel.objects.get(pk=pizza_id)
	pizza.delete()
	messages.success(request,'Pizza Has Been Deleted!')
	return redirect('adminhomepage')

def homepageview(request):
	context={}
	return render (request, 'homepage.html', context)

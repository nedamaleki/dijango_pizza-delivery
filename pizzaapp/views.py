from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

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
	return render (request, 'adminhomepage.html', {})
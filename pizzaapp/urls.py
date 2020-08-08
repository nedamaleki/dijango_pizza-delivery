from django.urls import path
from . import views
# from .views import adminloginpageview, adminhomepageview, authenticateadmin

urlpatterns = [
		path('adminlogin/', views.adminloginpageview, name='adminloginpage'),
		path ('authenticateadmin/', views.authenticateadmin, name=''),
		path('adminhomepage/', views.adminhomepageview, name='adminhomepage'),
		path ('adminlogout/', views.adminlogout, name='adminlogout'),
		path ('addpizza/', views.addpizza, name='addpizza'),
		path ('deletepizza/<pizza_id>', views.deletepizza, name='deletepizza'),
		path('', views.homepageview, name='homepage'),
		path('signupuser/', views.signupuser, name='signupuser'),
		path('userlogin/', views.userloginpageview, name='userloginpage'),
		path ('authenticateuser/', views.authenticateuser, name=''),
		path('userhomepage/', views.userhomepageview, name='userhomepage'),
		path ('userlogout/', views.userlogout, name='userlogout'),
		path ('placeorder/', views.placeorder, name='placeorder'),
		path ('userorders/', views.userorders, name='userorders'),
		path ('adminorders/', views.adminorders, name='adminorders'),
		path ('acceptorder/<order_id>', views.acceptorder, name='acceptorder'),
		path ('declineorder/<order_id>', views.declineorder, name='declineorder'),







		
		
]
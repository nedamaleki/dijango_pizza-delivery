from django.urls import path
from . import views
# from .views import adminloginpageview, adminhomepageview, authenticateadmin

urlpatterns = [
		path('admin/', views.adminloginpageview, name='adminloginpage'),
		path ('authenticateadmin/', views.authenticateadmin, name=''),
		path('adminhomepage/', views.adminhomepageview, name='adminhomepage'),
		path ('adminlogout/', views.adminlogout, name='adminlogout'),
		path ('addpizza/', views.addpizza, name='addpizza'),
		path ('deletepizza/<pizza_id>', views.deletepizza, name='deletepizza'),
		path('', views.homepageview, name='homepage'),
		
		
]
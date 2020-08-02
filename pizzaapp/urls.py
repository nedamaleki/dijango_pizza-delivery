from django.urls import path
from . import views
# from .views import adminloginpageview, adminhomepageview, authenticateadmin

urlpatterns = [
		path('', views.adminloginpageview, name='adminloginpage'),
		path ('authenticateadmin/', views.authenticateadmin, name=''),
		path('adminhomepage/', views.adminhomepageview, name='adminhomepage'),
		
		
]
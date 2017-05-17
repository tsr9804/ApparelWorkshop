from django.conf.urls import url
from . import views

urlpatterns = [
	# create URLS here
	url(r'^update/', views.update_db, name='update_db'),	
]
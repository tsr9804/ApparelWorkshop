from django.conf.urls import url
from home import views

urlpatterns = [
	# create URLS here
	url(r'^$', views.IndustrialView, name='index'),
	url(r'^IndustrialSewing', views.IndustrialView, name='industrial_sewing'),
	url(r'^HomeSewing', views.HomeView, name='home_sewing'),
	url(r'^Materials', views.MaterialsView, name='materials'),
	url(r'^Accessories', views.AccessoriesView, name='accessories'),
	url(r'^affiliatedisc', views.affiliatedisc, name='affiliatedisc')
]

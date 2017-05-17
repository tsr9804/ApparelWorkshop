from django.shortcuts import render
from django.template import loader	
from database.models import Product
from django.http import Http404


def IndustrialView(request):
	product_cat = 'Industrial Sewing Machine'
	try:		 
		product_list = Product().gather_top(product_cat)
	except:
		raise Http404("error in database")
	content = {'product_cat' : product_cat, 'product_list' : product_list}
	return render(request, 'home/index.html', content)

def HomeView(request):
	product_cat = 'Home Sewing Machine'
	try:		 
		product_list = Product().gather_top(product_cat)
	except:
		raise Http404("error in database")
	content = {'product_cat' : product_cat, 'product_list' : product_list}
	return render(request, 'home/index.html', content)
	

def MaterialsView(request):
	product_cat = 'Materials'
	try:		 
		product_list = Product().gather_top(product_cat)
	except:
		raise Http404("error in database")
	content = {'product_cat' : product_cat, 'product_list' : product_list}
	return render(request, 'home/index.html', content)

def AccessoriesView(request):
	product_cat = 'Accessories'
	try:		 
		product_list = Product().gather_top(product_cat)
	except:
		raise Http404("error in database")
	content = {'product_cat' : product_cat, 'product_list' : product_list}
	return render(request, 'home/index.html', content)

def affiliatedisc(request):
	return render(request, 'home/affiliatedisc.html')
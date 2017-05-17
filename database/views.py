from django.http import HttpResponse
from APIgrab import *
from DBupload import *
from models import *

def update_db(request):
	if Upload().uploadAll():   	
		return HttpResponse(status=200)
	else:
		return HttpResponse(status=500)
		
		


		#Product().gather_top("Industrial Sewing Machine")												
		#Product().gather_top("Materials")												
		#Product().gather_top("Home Sewing Machine")												
		#Product().gather_top("Accessories")	
		#Product().gather_top("Misc")												
		
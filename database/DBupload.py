# DBupload.py
#
#	Communicates with APIgrab.py. For moving data called from api in APIgrab.py to the database.
#
#

import APIgrab
import time
from APIgrab import Amazon
from models import *



class Upload:
	
#--------------------------Global Lists--------------------- 
	
	our_items = ['B0149GG9V4', 'B005I5DHPC', 'B00KAYDYE0', 'B005I5DS6U', 						#industrial
				 'B01ETX71I2', 																	#industrial
				 'B005I5DI56', 'B005C7EEQ2', 'B01I0M53GK', 'B003AJZZAS',						#industrial			
				 'B000JQM1DE', 'B003VWXZQ0', 'B003AVMZA4', 'B00JJ6L6PY', 						#home
				 'B00JBKVN8S', 'B003KK807M', 'B01E6SSMFG', 'B00T9B0G1Y', 						#home
				 'B003H3J50S', 'B00I12MDI6', 'B005GXPO70',										#overlock 
				 'B0014134IO', 'B00EJW5OTC', 'B003D7D8AQ', 'B01B8I7ORO',						#overlock
				 'B00T7ZNANS', 																	#overlock
				 'B000WOM50W', 'B00566E8DI', 'B001ELBCFG',										#general accessories
				 'B009D0O6LM', 'B00325ZJYC', 'B000YZ1Y06',										#general accessories
				 'B00BWXDHZY', 'B004OR14QE', 'B009D0O306',										#general accessories
				 'B001H61A6Y', 'B0046EBW1C', 'B0007XOEV6',										#general accessories
				 'B001UYSI8G', 'B00G6TZRUM', 													#gemera; accessories 
				 'B001ONRCL2', 'B003LANFXU', 'B001UYUTFQ', 'B001UYWWAQ',						#overlock accessories
				 'B0067YWEN4', 'B018K3C0WY', 'B00ARD7N8C', 										#overlock accessories															
				 'B00D980P14', 'B018V9HJJG',  													#overlock accessories
				 'B00D97XXIC', 																	#overlock accessories
				 'B01GWRGVGG', 'B01HLKLCFI', 'B003D0GODG',										#fabric
				 'B0144ARY5K', 'B008DYWJMW', 'B019RIWEEK', 										#fabric
				 'B00G28H9QW', 'B00MXBEIJI', 'B01CD3ORJQ',										#fabric
				 'B015YHXDJI', 'B0044FU8RC', 'B008DYWNB4', 										#faric
				 'B009K4MTII', 'B00W3EY1RY' 
				 ]													
	

	#our_items = ['B0149GG9V4', 'B005I5DHPC', 'B00KAYDYE0', 'B005I5DS6U'] 						#TEST

	#Keywords
	our_keywords = []											
#-----------------------------------------------------------	
	
	@classmethod
	def uploadByKeyword(self):
		products = {}

		for keywords in Upload.our_keywords:													#For all items to be updated:
			products.update(dict(Amazon().search_by_keywords(keywords).items()))  				#Add item to products.
			time.sleep(1)

		my_model = Product.objects.all()														#Instantiate our data model.
		

		#--------------------Redundancy Check----------------------
		for key in products.keys():																#List of keys for redundency check.
				if any(key == item.asin for item in my_model): 									#If a duplicate key is detected:														
					del products[key] 															#Remove the key from our products list.
					print "Duplicate key detected."	+ key										
				else:																			#Else:
					print "Key Succesfully added." + key										#Continue.																					
		#----------------------------------------------------------
		
		for key in products.keys():
			
			try:
				m1 = Product(asin = products[key]['asin'],										#Assign values to attributes of m1.
							 title = products[key]['title'], 
							 image = products[key]['image'],
							 price = products[key]['price'], 
							 currency = products[key]['currency'],
							 brand = products[key]['brand'],
							 model = products[key]['model'],
							 manufacturer = products[key]['manufacturer'], 
							 features = products[key]['features'],
							 itemURL = products[key]['itemURL'],
							 top_seller = False, 
							 category = products[key]['category'],
							 editorial = products[key]['editorial'],
							 editorial_short = products[key]['editorial'])

			except:
				print 'ERROR: Could not access dict elements'
				continue

			m1.save() 																			#Updates the database.	
		
		return True							



	@classmethod
	def uploadByID(self):
		products = {}																			#Instantiate products as a dictionary.
		
		for keywords in Upload.our_items:														#For all items to be updated:
			products.update(dict(Amazon().search_by_ID(keywords).items()))  					#Add item to products.
			time.sleep(1)

		my_model = Product.objects.all()														#Instantiate our data model.

		
		#--------------------Redundancy Check----------------------
		for key in products.keys():																#Make a list of keys for use in comparisson.
				if any(key == item.asin for item in my_model): 									#If a duplicate key is detected:														
					del products[key] 															#Remove it from our products list.
					print "Duplicate key detected."	+ key										
				else:																			#Else:
					print "Key Succesfully added." + key										#Continue.																								
		#----------------------------------------------------------
		
		for key in products.keys():																	
			try:
				m1 = Product(asin = products[key]['asin'],										#Assign values to attributes of m1.
							 title = products[key]['title'], 
							 image = products[key]['image'],
							 price = products[key]['price'],
							 currency = products[key]['currency'], 
							 brand = products[key]['brand'],
							 model = products[key]['model'],
							 manufacturer = products[key]['manufacturer'], 
							 features = products[key]['features'],
							 itemURL = products[key]['itemURL'],
							 top_seller = True,
							 category = products[key]['category'],
							 editorial = products[key]['editorial'],
							 editorial_short = products[key]['editorial_short']) 

			except:
				print 'ERROR: Could not access dict elements'
				continue

			m1.save() 																			#Update the database with m1.
		
		return True


	def uploadAll(self):
		Product.objects.all().delete()
		Upload.uploadByID()
		Upload.uploadByKeyword()
		return True

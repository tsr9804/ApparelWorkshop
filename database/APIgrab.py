# APIgrab.py
#
#	Calls our affilaite APIs for item listing attributes.
#	The results will then be sent to DBupload.py to be entered into our DB.
#	That data will then be used in views.py to be represented on the page.

from django.utils.text import Truncator
from amazon.api import AmazonAPI 
import re

TAG_RE = re.compile(r'<[^>]+>')

class Amazon:

	api = AmazonAPI(ID, KEY, USER)

	def add_product(self, product, product_dict):

		if Amazon().is_valid(product):
			imgURL = product.large_image_url.replace('http://ecx.', 'https://images-na.ssl-')
			product_dict[product.asin] = {'asin' : product.asin,										#add product to dictionary															
										  'title' : product.title,             							#product ID is the key and dictionary containing attributes is the value
										  'image' : imgURL,							
										  'price' : product.price_and_currency[0],
										  'currency': product.price_and_currency[1],
										  'brand' : product.brand,
										  'model' : product.model,
										  'manufacturer' : product.manufacturer,
										  'features' : product.features,
										  'itemURL' : product.offer_url,
										  'top_seller' : True, 											#arbitrary value assignment (overwritten) 
										  'category' :  Amazon().get_category(product),
										  'editorial': Amazon().remove_tags(Amazon().truncate_editorial(product.editorial_review)),
										  'editorial_short': Amazon().remove_tags(Amazon().truncate_editorial_short(product.editorial_review))} #grabs editorial and strips html from it

		else:
			print 'Product denied, vital data N/A.' + product.asin			

																									#categorizes a product based on its browse nodes  
	

	def truncate_editorial(self, text):
		short_text = text[:1000] + (text[1000:] and '.')
		return short_text

	def truncate_editorial_short(self, text):
		short_text = text[:150] + (text[75:] and '...')
		return short_text

	def remove_tags(self, text):
		return TAG_RE.sub('', text)

	def get_category(self, product):
		
		nodes_list = []																				#will hold names of nodes associated w/ a product
		industrial_machine = 'Industrial Machines'
		parts = 'Parts'
		home_machine = 'Sewing Machines'
		tools_accessories = 'Tools & Accessories'
		supplies = 'Sewing Supplies'
		fabric = 'Fabric'

		for node in product.browse_nodes:
			nodes_list.extend(node.name)															#at this point the the node has a list with all its associated keywords

		if fabric in nodes_list:
			return 'Materials'

		elif home_machine in nodes_list:															#now we want to assign it a category based on the keywords
			return 'Home Sewing Machine'
		
		elif industrial_machine in nodes_list:
			return 'Industrial Sewing Machine'
		
		elif tools_accessories in nodes_list: 	
			return 'Accessories'

		elif supplies in nodes_list:
			return 'Materials'
	
		else:
			return 'Accessories'
		
		#Industrial Machine Node Names: Industrial Machines, Parts
		#Home Machine Node Names: Sewing Machines
		#Accesory Node Names: Tools & Accesories
		#Materials Node Names: Sewing Supplies, Fabric
			
	def is_valid(self, product):
		key = product.large_image_url
		price = product.price_and_currency[0]

		if not key: 
			return False 
		elif not price:
			return False
		else:
			return True #key


	def insert(self, products, product_dict):
		try:
			for product in products:
				Amazon().add_product(product, product_dict)   										#add products to dictionary
		except:
			return					

	def search_by_keywords(self, *args):
		argument_list = list(args)       															#construct argument list
		product_dict = {}				  															#dictionary to store products
		
		for key in argument_list:
			products = Amazon.api.search(Keywords = key, SearchIndex = 'All')   					#iterable object containing products
			Amazon().insert(products, product_dict)
		return product_dict

	def search_by_ID(self, *args):
		argument_list = list(args)       															#create argument list
		num_arguments = len(argument_list)															#number of products to search
		product_dict = {}			     															#dictionary to store products
		ID_string = ','.join(argument_list)															#String containing IDs
		
		if num_arguments > 1:
			products = Amazon.api.lookup_bulk(ItemId = ID_string)   								#list of product objects
			Amazon().insert(products, product_dict)
		else:
			try:
				product = Amazon.api.lookup(ItemId = ID_string)   									#single product object
				Amazon().add_product(product, product_dict)   										#add products to dictionary
			except Exception,e: 
				print str(e)
				return product_dict
		return product_dict

import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from shop.models import Product, Category

from django.db.models import Count, Sum
from django.db.models.functions import Lower



#Convert datetimes into str for JSON Dump
class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        return super(LazyEncoder, self).default(obj)

def charts(request):
	
	#--------------------------------------------
	#CREATE Chart for number of category products
	#--------------------------------------------
	#Count how many category objects per distinct category
	dataset = \
	Product.objects.values('category')\
	       .order_by('category')\
	       .annotate(count=Count('category'))
	
	# Create lists
	categories = list()
	count_series = list()
	# Append the values & formatting
	for entry in dataset:
		# categories.append(entry['category'])
		categories=list(Category.objects.values_list('name'))

		count_series.append(entry['count'])
		
	# Highcharts Configuration
	count_series = {
		'name': 'Products',
		'data': count_series
 	}
	
	chart1 = {
		'chart': {
			'type':'column', 
			'borderRadius': 20,
		    'borderWidth':2,
		    'marginTop':50,
		    'marginLeft':65,
		    'marginRight':10
		},
		'credits': {
			'position':{
			   'align':'left','x':50}
		},     	  
		'title': {
			'text':'Mahsulotlar soni'
		},
	    'legend': {
	    	'enabled':'false'
	    },
		'yAxis': {
			'title': {
				'text':'Soni'}
		},
		'xAxis': {
			'categories':categories
		},
	 	'series': [
	 		count_series
	 	],
		'plotOptions': {
			'series':{
				'borderRadius': 5,
				'colorByPoint':'true'
			},
		    'column':{
		    	'groupPadding':0,
		    	'pointPadding':0.1
		    }
		},
	}
	
	# Convert to JSON
	dump1 = json.dumps(chart1)
	
	#-----------------------------------------
	#CREATE Chart for number of orders by date
	#-----------------------------------------
	#Count how many date objects per distinct date

 

	return render(request, 'charts.html', {'chart1': dump1})
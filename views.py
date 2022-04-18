from django.shortcuts import render
from django.http import HttpResponse
import json
def index(request):

	data = {
		'Message': 'Hello World, I am Vijay! '}
	return HttpResponse(json.dumps(data),content_type="application/json")
# Create your views here.

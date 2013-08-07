from django.http import HttpResponse
from django.shortcuts import render

# Vue main
def index(request):
	return render(request, 'website/index.html')
	#return HttpResponse("Hello World")


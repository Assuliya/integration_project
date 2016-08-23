from django.shortcuts import render, HttpResponse
from datetime import datetime

def index(request):
	print datetime.now()

	context = {
    "date": datetime.now()
    }
	return render(request, 'base_time/index.html', context)
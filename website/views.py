from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request, 'website/home.html')

def about(request):
	return render(request, 'website/about.html')

def schedule(request):
	return render(request, 'website/schedule.html')

def ticket(request):
	return render(request, 'website/ticket.html')

def gallery(request):
	return render(request, 'website/gallery.html')

def info(request):
	return render(request, 'website/info.html')

def contact (request):
	return render(request, 'website/contact.html')

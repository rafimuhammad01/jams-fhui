from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	context = {'page':'home'}
	return render(request, 'website/home.html', context)

def about(request):
	context = {'page':'about'}
	return render(request, 'website/about.html', context)

def schedule(request):
	context = {'page':'schedule'}
	return render(request, 'website/schedule.html', context)

def ticket(request): #not used
	context = {'page':'ticket'}
	return render(request, 'website/ticket.html', context)

def gallery(request):
	context = {'page':'gallery'}
	return render(request, 'website/gallery.html', context)

def info(request):
	context = {'page':'info'}
	return render(request, 'website/info.html', context)

def contact (request):
	context = {'page':'contact'}
	return render(request, 'website/contact.html', context)

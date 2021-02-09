from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
import os
import requests

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

def getRecentPosts(request):
	if request.is_ajax():
		data_id_json = requests.get('https://graph.instagram.com/me/media?fields=id&access_token=' + os.environ.get('SECRET_INSTA_KEY')).json()
		posts = []
		for i in range(5):
			post_id = data_id_json['data'][i]['id']
			post_detail = requests.get('https://graph.instagram.com/' + post_id + '?fields=id,media_type,media_url,caption,permalink,thumbnail_url,timestamp,username&access_token=' + os.environ.get('SECRET_INSTA_KEY')).json()
			posts.append(post_detail)
		return JsonResponse(posts, safe=False)
	else:
		return HttpResponseNotFound


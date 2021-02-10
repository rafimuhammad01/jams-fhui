from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
import os
import requests

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

def getRecentPosts(request):
	if request.is_ajax():
		INSTA_KEY = 'IGQVJWMDRnWnZAJTmlnWm9lM2NmRDJLNHFjeUdNT2ZAWaEI5OV9rZAEZA1WHpOei1wVlAxQmNJTVlxM2pkUnVWRDhYMnR0a3FQU0pIUUo4QlMwdGRQdEoxTjVLVTBWVlZAtbmxMNjVXMlhHQTZAjZAVlFeG9FMwZDZD'
		data_id_json = requests.get('https://graph.instagram.com/me/media?fields=id&access_token=' + INSTA_KEY).json()
		posts = []
		for i in range(6):
			post_id = data_id_json['data'][i]['id']
			post_detail = requests.get('https://graph.instagram.com/' + post_id + '?fields=id,media_type,media_url,caption,permalink,thumbnail_url,timestamp,username&access_token=' + INSTA_KEY).json()
			posts.append(post_detail)
		return JsonResponse(posts, safe=False)
	else:
		return HttpResponseNotFound

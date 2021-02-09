from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('schedule/', views.schedule, name='schedule'),
    path('ticket/', views.ticket, name='ticket'),
    path('gallery/', views.gallery, name='gallery'),
    path('info/', views.info, name='info'),
    path('contact/', views.contact, name='contact'),
    path('fetcher/', views.getRecentPosts, name='getRecentPosts')
]
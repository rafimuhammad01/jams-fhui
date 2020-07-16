from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lineup/', views.lineup, name='lineup'),
    path('schedule/', views.schedule, name='schedule'),
    path('ticket/', views.ticket, name='ticket'),
    path('gallery/', views.gallery, name='gallery'),
    path('info/', views.info, name='info'),
    path('contact/', views.contact, name='contact'),
]


from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name = 'index'),
    path("contact", views.contact, name = 'contact'),
    path('services', views.services, name = 'services'),
    path('Aboutus', views.Aboutus, name = 'Aboutus'),
    path('post/<str:pk>', views.post, name = 'post')
    
]


from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from webon.models import Contact
from .models import Post
from django.contrib import messages

# Create your views here.
def index(request):
    posts = Post.objects.all()
    # messages.success(request, 'this is the test message')
    return render(request, 'index.html', {'posts':posts})

def post(request,pk):
    posts = Post.objects.get(id = pk)
    return render(request,'post.html',{'posts':posts})

def Aboutus(request):
    return render(request,'about.html')
    


def services(request):
    return render(request, "services.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')


from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from . import models

# Create your views here.

def home(request):
    about = models.About.objects.all()
    return render(request, 'pages/home.html', {'about': about})

def about_me(request):
    about = models.About.objects.all()
    return render(request, 'pages/about.html', {'about': about})

def contact_me(request):
    reach = models.Contact.objects.all()
    return render(request, 'pages/contact.html', {'reach': reach})

def my_portfolio(request):
    projects  = models.Portfolio.objects.order_by('-date')
    return render(request, 'pages/portfolio.html', {'projects': projects})

def project_detail(request, pk):
    post = get_object_or_404(models.Portfolio, pk=pk)
    return render(request, 'pages/project_detail.html', {'post': post})

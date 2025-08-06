from django.shortcuts import render,HttpResponse
from .models import*
# Create your views here.

def dashboard(request):
    clients = Clientinfo.objects.all()
    return render(request,"clients_dashboard.html",{"show_clients":clients})

def manage(request):
    clients = Clientinfo.objects.all()
    return render(request,"clients_manage.html",{"show_clients":clients})

    
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def donor_login(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['username'],
                            password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('/donor/dashboard/')
    return render(request, 'donor/login.html')

@login_required
def donor_dashboard(request):
    return render(request, 'donor/dashboard.html')

@login_required
def blood_request(request):
    if request.method == "POST":
        BloodRequest.objects.create(
            patient=Patient.objects.get(user=request.user),
            reason=request.POST['reason'],
            blood_group=request.POST['blood_group'],
            unit=request.POST['unit']
        )
        return redirect('/')
    return render(request, 'patient/request.html')

@login_required
def admin_requests(request):
    requests = BloodRequest.objects.all()
    return render(request, 'admin/request_history.html', {'requests': requests})

@login_required
def blood_stock(request):
    stocks = BloodStock.objects.all()
    return render(request, 'admin/blood_stock.html', {'stocks': stocks})


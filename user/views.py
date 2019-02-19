from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    return render(request, 'register.html', {'title': 'Login'})


@login_required()
def dashboard(request):
    return render(request, 'home/dashboard.html', {'title': 'Home'})

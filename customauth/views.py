from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def profile(request):

    if not request.user.is_authenticated:
        return HttpResponse("You are not logged in. Please log in to access your profile.")



    context = {} 
    return render(request, 'customauth/profile.html',context)

def profilee(request):
    if not request.user.is_authenticated:
        return HttpResponse("You are not logged in")
    context = {
        'message': f"Welcome {request.user.username}!"
    }
    return render(request, 'customauth/profile.html', context)

@login_required(login_url='login')
def dashboard(request):
    return HttpResponse("Welcome to the dashboard!")
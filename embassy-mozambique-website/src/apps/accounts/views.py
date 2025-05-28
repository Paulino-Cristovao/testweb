from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    return HttpResponse("<h1>Login</h1><p>Login functionality coming soon.</p><p><a href='/admin/'>Use Admin Login</a></p>")

def logout_view(request):
    logout(request)
    return redirect('/')

def register_view(request):
    return HttpResponse("<h1>Register</h1><p>Registration functionality coming soon.</p>")

@login_required
def profile_view(request):
    return HttpResponse(f"<h1>Profile</h1><p>Welcome {request.user.username}!</p>")

from .models import Tenant
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm, NewAssetForm

# Create your views here.

def homepage(request):
  return render(request = request,
               template_name="main/homepage.html",
               context={"Tenant": Tenant.objects.all})

def register(request):
  if request.method == "POST":
    form = NewUserForm(request.POST)
    if form.is_valid():
     user = form.save()
     username = form.cleaned_data.get('owner_name')
     messages.success(request, f"New Account Created: {username}")
     login(request,user)
     messages.info(request, f"You are now logged in as {username}")
     return redirect("main:homepage")
    
    else:
      for msg in form.error_messages:
       messages.error(request, f"{msg}:{form.error_messages[msg]}")
    
  form = NewUserForm
  return render(request,
                "main/register.html",
                context={"form":form})

def login_request(request):
   if request.method == "POST":
    form = AuthenticationForm(request, data = request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      passeword = form.cleaned_data.get('password')
      user = authenticate(username = username, passeword = passeword)
      if user is not None:
        login(request, user)
        messages.info(request, f"You are now logged in as {username}")
        return redirect("main:homepage")
    
      else:
        messages.error(request, "Invalid username or password")

    else:
      messages.error(request, "Invalid username or password")
   
   form = AuthenticationForm()
   return render(request,
                "main/login.html",
                {"form":form})

def logout_request(request):
  logout(request)
  messages.info(request, "Logged out successfully !")
  return redirect("main:homepage")

def new_asset(request):
  if request.method == "POST":
    form = NewAssetForm(request.POST)
    if form.is_valid():
     asset = form.save()
     assetName = form.cleaned_data.get('asset_adress')
     messages.success(request, f"New Asset Added: {assetName}")
     return redirect("main:homepage")
    
    else:
      for msg in form.error_messages:
       messages.error(request, f"{msg}:{form.error_messages[msg]}")
    
  form = NewAssetForm
  return render(request,
                "main/new_asset.html",
                context={"form":form})

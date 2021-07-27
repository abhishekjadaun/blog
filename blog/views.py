from django.contrib.auth import authenticate,logout,login
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from .forms import SignUpForm,UserLogin
from django.contrib import messages
def auth_login(request):
   if not request.user.is_authenticated:
      if request.method=="POST":
         login_form=UserLogin(request=request,data=request.POST)
         if login_form.is_valid():
            uname=login_form.cleaned_data['username']
            upass=login_form.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
               login(request,user)
               return HttpResponseRedirect('/blog/')

      else:
         login_form=UserLogin()         
      params={
         'form':login_form
      }  
      return render(request,'login.html',params)
   else:
      return HttpResponseRedirect('/blog/')
  

def signup(request):
   if request.method=="POST":
      form=SignUpForm(request.POST)
      if form.is_valid():
         form.save()
         messages.success(request,'You are Successfully Registered')
   else:
      form=SignUpForm()

   params={
      'form':form,
   }
   return render(request,'signup.html',params)

def user_logout(request):
   logout(request)
   return HttpResponseRedirect('/')

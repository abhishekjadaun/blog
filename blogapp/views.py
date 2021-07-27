from django.http.response import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from .models import BlogModel
# Create your views here.
def index(request):
       data=BlogModel.objects.all()
       if request.user.is_authenticated:

              return render(request,'blogapp/index.html',{'data':data})
       else:
              return HttpResponseRedirect('/')


from django.shortcuts import render

# Create your views here.
def home(request , groupname):
    return render(request , 'myapp/home.html',{'groupname':groupname})
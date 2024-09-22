from django.shortcuts import render
from .models import Chat , Group
# Create your views here.
def home(request , groupname):
    group = Group.objects.filter(group_name = groupname).first()
    chat=[]
    if group:
        chat = Chat.objects.filter(group_name=group)
    else:
        group = Group(group_name = groupname)  
        group.save()
    return render(request , 'myapp/home.html',{'groupname':groupname , 'chats':chat})
from django.contrib import admin

from .models import Chat, Group

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['id','contant','group_name','timestamp']

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id','group_name']
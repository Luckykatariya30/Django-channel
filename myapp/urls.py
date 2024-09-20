from django.urls import path
from myapp import views


urlpatterns = [
    path('<str:groupname>/',views.home),
]


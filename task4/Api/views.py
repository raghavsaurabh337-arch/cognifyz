from django.shortcuts import render,redirect
from .models import home
from .serializers import homeSerializer
from rest_framework.viewsets import  ModelViewSet


# Create your views here.
def home(request):
     return render(request,'home.html')
def view(request):
     return render(request,'views.html')



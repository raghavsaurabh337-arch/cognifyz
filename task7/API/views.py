from django.shortcuts import render,redirect
from .models import recode,create
from .serializers import recodeSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView
import email


# Create your views here.
def create_account(request):
     if request.method=="POST":
          name=request.POST['name']
          email=request.POST['email']
          password=request.POST['password']
          create.objects.create(name=name, email=email, password=password) 
          return redirect('login')
     return render(request, 'create_account.html')

def login(request):
     if request.method=="POST":
          email=request.POST['email']
          password=request.POST['password']
          user= create.objects.filter(
               email=email,
               password=password
               ).first()
          if user is None:
               return redirect('create_account')
          else:
               return redirect('home')
     return render(request, 'login.html')
def home(request):
     if request.method=="POST":
          name=request.POST['name']
          email=request.POST['email']
          message=request.POST['message']
          recode.objects.create(name=name, email=email, message=message)
     return render(request,'home.html')
def view(request):
     recodes =recode.objects.all()
     return render(request,'views.html',{"recodes":recodes})


class GCrecode(ListModelMixin,CreateModelMixin,GenericAPIView):
     queryset=recode.objects.all()
     serializer_class=recodeSerializer
     authentication_classes = [SessionAuthentication]
     permission_classes = [IsAuthenticated]
     def get(self,request,*args,**kwargs):
          return self.list(request,*args,**kwargs)
     def post(self,request,*args,**kwargs):
          return self.create(request,*args,**kwargs)
class RUDrecodeAPI(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,GenericAPIView):
     queryset=recode.objects.all()
     serializer_class=recodeSerializer
     authentication_classes = [SessionAuthentication]
     permission_classes = [IsAuthenticated]
     def get(self, request, *args, **kwargs):
          return self.retrieve(request, *args, **kwargs)

     def put(self, request, *args, **kwargs):
          return self.update(request, *args, **kwargs)

     def patch(self, request, *args, **kwargs):
          return self.partial_update(request, *args, **kwargs)

     def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



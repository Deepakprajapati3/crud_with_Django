from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import User
from .forms import Student_Registration

# Create your views here.

def show_data(request):
    if request.method=='POST':
        fm=Student_Registration(request.POST)
        if fm.is_valid():
           nm=  fm.cleaned_data['name']
           em=  fm.cleaned_data['email']
           pw= fm.cleaned_data['password']
           reg=User(name=nm,email=em,password=pw)
           reg.save()
           fm=Student_Registration()
            
            
    else:
        fm=Student_Registration() 
    data=User.objects.all()   
    return render(request,'addandshow.html',{'form':fm,'Data':data})





def update_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=Student_Registration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect("/") 
    else:
        pi=User.objects.get(pk=id)   
        fm=Student_Registration(instance=pi)
    return render(request,"update.html",{"form":fm})
    
    
    



def delete_data(request, id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')



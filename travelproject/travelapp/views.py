from django.shortcuts import render

from .models import place,employee

# Create your views here.

def demo(request):
    obj=place.objects.all()
    obj1=employee.objects.all()
    return render(request,'index.html',{'result':obj,'emp':obj1})
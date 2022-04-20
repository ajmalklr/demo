from django.shortcuts import HttpResponse, render, redirect
from .models import movie
from .forms import MovieForm

# Create your views here.

def index(request):
    obj=movie.objects.all()
    content={
        'movie_list' : obj
    }
    return render(request,'index.html',content)

def detail(request,movie_id):
    id=movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie':id})

def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']
        mov=movie(name=name,desc=desc,year=year,img=img)
        mov.save()
    return render(request,'add.html')

def update(request,id):
    movi=movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movi)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'movi':movi,'form':form})

def delete(request,id):
    if request.method=='POST':
        movi=movie.objects.get(id=id)
        movi.delete()
        return redirect('/')
    return render(request,'delete.html')

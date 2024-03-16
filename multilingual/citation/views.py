from django.shortcuts import render
from django.http import HttpResponse
import openpyxl,os
from django.conf import settings
from .models import sindhi,northeast,malayalam



def home(request):
    return render(request,"citation/home.html")

def Sindhi(request):
    obj=sindhi.objects.all()
    context={"data":obj}
    if request.method=="POST":
        searched=request.POST.get("search")
        # searche=searched.upper()

        i=request.POST.get("type_of_search")
        j=int(i)
        if(j==1):
            context['data']=sindhi.objects.filter(title__icontains=searched)
        elif j==2:
            context['data']=sindhi.objects.filter(accession_number__icontains=searched)
        elif j==3:
            context['data']=sindhi.objects.filter(author_first_name__icontains=searched)
        elif j==4:
            context['data']=sindhi.objects.filter(author_last_name__icontains=searched)
        elif j==5:
            context['data']=sindhi.objects.filter(keyword__icontains=searched)
        elif j==6:
            context['data']=sindhi.objects.filter(publisher__icontains=searched)
        elif j==7:
            context['data']=sindhi.objects.filter(place__icontains=searched)
        return render(request,"citation/sindhi.html",context=context)
        
    return render(request,"citation/sindhi.html",context=context)
def Northeast(request):
    obj=northeast.objects.all()
    context={
        "data": obj
    }
    if request.method=="POST":
        searched=request.POST.get("search")
        # searche=searched.upper()

        i=request.POST.get("type_of_search")
        j=int(i)
        if(j==1):
            context['data']=northeast.objects.filter(title__icontains=searched)
        elif j==2:
            context['data']=northeast.objects.filter(accession_number__icontains=searched)
        elif j==3:
            context['data']=northeast.objects.filter(class_number__icontains=searched)
        elif j==4:
            context['data']=northeast.objects.filter(author_name__icontains=searched)
        elif j==5:
            context['data']=northeast.objects.filter(year__icontains=searched)
        elif j==6:
            context['data']=northeast.objects.filter(publisher__icontains=searched)
        elif j==7:
            context['data']=northeast.objects.filter(collection__icontains=searched)
        elif j==8:
            context['data']=northeast.objects.filter(language__icontains=searched)
        return render(request,"citation/northeast.html",context=context)
    return render(request,"citation/northeast.html",context=context)
def Malayalam(request):
    obj=malayalam.objects.all()
    context={
        "data": obj
    }
    if request.method=="POST":
        searched=request.POST.get("search")
        # searche=searched.upper()

        i=request.POST.get("type_of_search")
        j=int(i)
        if(j==1):
            context['data']=malayalam.objects.filter(malayalam_title__icontains=searched)
        elif j==2:
            context['data']=malayalam.objects.filter(engish_title__icontains=searched)
        elif j==3:
            context['data']=malayalam.objects.filter(isbn_no__icontains=searched)
        elif j==4:
            context['data']=malayalam.objects.filter(author_name__icontains=searched)
        elif j==5:
            context['data']=malayalam.objects.filter(subject__icontains=searched)
        elif j==6:
            context['data']=malayalam.objects.filter(genre__icontains=searched)
        elif j==7:
            context['data']=malayalam.objects.filter(publisher__icontains=searched)
        elif j==8:
            context['data']=malayalam.objects.filter(year_of_dc__icontains=searched)
        elif j==9:
            context['data']=malayalam.objects.filter(year_of_pub__icontains=searched)
        return render(request,"citation/malayalam.html",context=context)
    return render(request,"citation/malayalam.html",context=context)

def sindhidesc(request,id):
    obj=sindhi.objects.filter(id=id)[0]
    context={
        'data':obj
    }
    return render(request,"citation/sindhidesc.html",context)

def northeastdesc(request,id):
    obj=northeast.objects.filter(id=id)[0]
    context={
        'data':obj
    }
    return render(request,"citation/northeastdesc.html",context)

def malayalamdesc(request,id):
    obj=malayalam.objects.filter(id=id)[0]
    context={
        'data':obj
    }
    return render(request,"citation/malayalamdesc.html",context)
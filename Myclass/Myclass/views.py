from django.http import HttpResponse
from django.shortcuts import render

def Forms(request):
    params={}
    return render(request,"form.html",params)

def showname(request):
    params={
    "first_name" : request.GET.get("first_name"),
    "last_name" : request.GET.get("last_name"),
    "Phone_number" : request.GET.get("Phone_number"),
    "email" : request.GET.get("email"),
    "password" : request.GET.get("password"),
    "date" : request.GET.get("date"),
    "youtube" : request.GET.get("youtube"),
    }
    return render(request,"showdata.html",params)
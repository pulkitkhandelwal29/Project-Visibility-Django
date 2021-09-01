from django.shortcuts import render,redirect

from .visibilitypython import *

def home(request):
    global source_path
    source_path = "/media/sample.mp3"
    if request.method=='POST':
        text = request.POST.get('text')
        confidence = request.POST.get('confidence')
        url_returned = request.POST.get('url')
        print(url_returned)
        if url_returned == 'http://127.0.0.1:8000/':
            url_returned = 'home'

        url = 'http://localhost:8000'
        if text:
            source_path,temp_input = program(url,text)
            if temp_input == 'stop':
                url_returned = url_returned.split('/')[-1]
                print(url_returned)
                return redirect(url_returned)
            return redirect(temp_input)

    if request.method=='GET':
        return render(request,'home.html',{'source_path':source_path})

def about(request):
    if request.method=='GET':
        print(source_path)
        return render(request,'about.html',{'source_path':source_path})

def howtouse(request):
    if request.method=='GET':
        print(source_path)
        return render(request,'howtouse.html',{'source_path':source_path})

def motivation(request):
    if request.method=='GET':
        print(source_path)
        return render(request,'motivation.html',{'source_path':source_path})

def beneficiary(request):
    if request.method=='GET':
        print(source_path)
        return render(request,'beneficiary.html',{'source_path':source_path})

def technologies(request):
    if request.method=='GET':
        print(source_path)
        return render(request,'technologies.html',{'source_path':source_path})

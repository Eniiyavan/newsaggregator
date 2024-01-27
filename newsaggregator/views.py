from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from . import timesof
from django.template import Context,loader
from flask import jsonify,request
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def display_data(request):
    if(request.method=='POST'):
        city=request.POST.get('city')
        a=timesof.send_Data(city)
        return render(request,'hello.html',{'data':a})
    else:
        a=timesof.send_Data(' ')
        return render(request,'hello.html',{'data':a})

@csrf_exempt
def scrape(request):
    url1=request.GET.get('url','')
    a=timesof.send_specific(url1)
    b= render(request,'specific.html',{'data':a})
    return b
    #return redirect('specific_page', content=a['content'], img_url=a['img_url'], content_url=a['content_url'])
    #return JsonResponse({"titles":a})

def specific_page(request, data):
    content = request.GET.get('content', '')
    img_url = request.GET.get('img_url', '')
    content_url = request.GET.get('content_url', '')

    return render(request, 'specific.html', {'content': content, 'img_url': img_url, 'content_url': content_url})



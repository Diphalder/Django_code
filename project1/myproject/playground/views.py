from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

# Create your views here.
# rqst -> responds
# rqsr handler
# action 

def say_hello(request):
    # pull data form db
    # transform
    # send email
    return HttpResponse('hello world')

def renderhtmlfile(request):
    # pull data form db
    # transform
    # send email
    return render(request,'hello.html' , { 'nameVar' : 'Dip Halder'})


def playground(request):
  template = loader.get_template('hello.html')
  return HttpResponse(template.render())



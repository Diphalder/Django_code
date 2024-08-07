from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

from .models import Member

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

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {'mymembers': mymembers,}
  return HttpResponse(template.render(context, request))



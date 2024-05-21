from django.shortcuts import render
from members.models import members
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def show_members(request):
    all_members=members.objects.all()
    template=loader.get_template("memberss.html")
    context={
        'all_members':all_members
    }
    return HttpResponse(template.render(context,request))
    
def member_details(request,id):
    req_member=members.objects.get(id=id)
    template=loader.get_template("member_detail.html")
    context={
        'member':req_member,
    }
    return HttpResponse(template.render(context,request))
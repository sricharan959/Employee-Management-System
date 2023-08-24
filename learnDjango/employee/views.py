from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Employee,BlogPosts
from django.db.models import Q
# Create your views here.
def index(request):
    myEmployees=Employee.objects.all().order_by('name')
    template=loader.get_template('employee/index.html')
    context={
        'myEmployees':myEmployees
    }
    return HttpResponse(template.render(context,request))

def create(request):
    template=loader.get_template("employee/createPage.html")
    return HttpResponse(template.render({},request))

def createData(request):
    data1=request.POST["name"]
    data2=request.POST["title"]
    newEmployee=Employee(name=data1,title=data2)
    newEmployee.save()
    return HttpResponseRedirect(reverse('employee'))

def delete(request,id):
    deleteEmployee=Employee.objects.get(id=id)
    deleteEmployee.delete()
    return HttpResponseRedirect(reverse('employee'))

def update(request,id):
    updateEmployee=Employee.objects.get(id=id)
    template=loader.get_template("employee/updatePage.html")
    context={
        'Employee':updateEmployee
    }
    return HttpResponse(template.render(context,request))

def updateData(request,id):
    data1=request.POST['name']
    data2=request.POST['title']
    updateEmployee=Employee.objects.get(id=id)
    updateEmployee.name=data1
    updateEmployee.title=data2
    updateEmployee.save()
    return HttpResponseRedirect(reverse('employee'))

def blog(request):
    posts=BlogPosts.objects.all()
    featuredposts=BlogPosts.objects.all().filter(featured=True)
    template=loader.get_template('employee/blog.html')
    context={
        'posts':posts,
        'featuredposts':featuredposts
    }
    return HttpResponse(template.render(context,request))
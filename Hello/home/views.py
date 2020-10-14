from django.shortcuts import render,HttpResponse
from django.template import RequestContext
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    # context={
    #     'variable':'this is sent'
    # }
    #messages.success(request,'This is a Test message.')
    return render(request,'index.html')
    #return HttpResponse("This is homepage")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is about page")

def service(request):
    return render(request, 'service.html')
    #return HttpResponse("This is service page")

# makemigrations - create changes and store in a file
# migrate - apply the pending changes created by migrations

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your data is uploaded!')
    return render(request, 'contact.html')
    #return HttpResponse("This is contact page")
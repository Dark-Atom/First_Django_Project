from django.shortcuts import render ,HttpResponse
from datetime import datetime
from first.models import Contact
# Create your views here.
def index(request):
    
    #return HttpResponse("this is home page")
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def Contactus(request):
    if request.method == "POST":
        name =request.POST.get('uname')
        number =request.POST.get('number')
        email =request.POST.get('email')
        des =request.POST.get('des')
        contact = Contact(name = name, number=number , email=email, des=des, date = datetime.today())
        contact.save()
    return render(request, "contactus.html")

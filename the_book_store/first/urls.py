from django.contrib import admin
from django.urls import path
from first import views

admin.site.site_header = "The Book Store Admin"
admin.site.site_title = "The Book Store Admin Portal"
admin.site.index_title = "Welcome to Book Store Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index, name="home"),    
    path("about",views.about, name="about"),  
    path("contactus",views.Contactus, name="contactus")    
        
]

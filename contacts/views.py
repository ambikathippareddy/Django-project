from django import contrib
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from . models import contacts
from django.contrib import admin, messages
from django.contrib.auth.models import User

# Create your views here.

def inquiry(request):
    if request.method =='POST':
        car_id=request.POST['car_id']
        car_title=request.POST['car_title']
        user_id=request.POST['user_id']
        first_name =request.POST['first_name']
        last_name=request.POST['last_name']
        customer_need=request.POST['customer_need']
        city=request.POST['city']
        state=request.POST['state']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']

        if request.user.is_authenticated:

            has_contacted=contacts.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request,'you have already inquired about this car, we will get back to you shortly')
                return redirect('/cars/'+car_id)

        contact=contacts(car_id=car_id, car_title=car_title, user_id=user_id,first_name=first_name, last_name=last_name,
        customer_need=customer_need, city=city, state=state, email=email, phone=phone, message=message)
        
        admin_info =User.objects.get(is_superuser=True)
        admin_email=admin_info.email

        
        send_mail(
                    'now car inquiry onn our website',
                   'you have a car enquiry for the car'+car_title +'.login to your admin panel for more details',
                   'ambika.thipareddy@gmail.com',
                   [admin_email],
                   fail_silently=False,
        )
        contact.save()
        messages.success(request, "your request has been submitted")
        return redirect('/cars/'+car_id)
   
    

    

import email
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import Booking
from mysite.models import booking


# Create your views here.
# def booking(request):
#     if request.method == "POST":
#         form = Booking(request.POST)
#         if form.is_valid():
#             form.save()
#             first_name = form.cleaned_data['fname']
#             last_name = form.cleaned_data['lname']
#             email = form.cleaned_data['email']
#             phone = form.cleaned_data['phone']
#             address = form.cleaned_data['address']
#             zip_code = form.cleaned_data['zip_code']
#             message = form.cleaned_data['message']
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             messages.success(request, ("Message Sent Successful!"))
#             return redirect('contact')

#     else:
#         form = Booking()
 
#     return render(request, 'contact.html', {
#         'form':form,
#     })


def saveEnquiry(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        message = request.POST.get('message')

        en=booking(first_name=fname,last_name=lname,email_address=email,phone=phone,address=address,zip_code=zip_code,message=message)
        en.save()


    return render(request, "contact.html")



# def saveform(request):
#     if request.method == "POST":
#         first_name = request.POST.get('fname')
#         last_name = request.POST.get('lname')
#         email_address = request.POST.get('email')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         zip_code = request.POST.get('zip_code')
#         message = request.POST.get('message')

#         en=booking(first_name=first_name, last_name=last_name, email_address=email_address, phone=phone, address=address, zip_code=zip_code, message=message)
#         en.save()

#     return render(request, 'contact.html', {})



    

def index(request):
    return render(request, 'index.html', {}) 

def about(request):
    return render(request, 'about.html', {}) 

def contact(request):
    return render(request, 'contact.html', {}) 

def service(request):
    return render(request, 'service.html', {}) 

def project(request):
    return render(request, 'project.html', {}) 

def blog(request):
    return render(request, 'blog.html', {}) 

def single(request):
    return render(request, 'single.html', {}) 

def feedback(request):
    return render(request, 'feedback.html', {}) 


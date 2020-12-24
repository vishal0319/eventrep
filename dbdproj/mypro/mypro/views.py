from django.shortcuts import render
from mypro.models import Student
from django.contrib import messages

def stdrecord(request):
    if request.method=="POST":
        if request.POST.get('Student_name') and request.POST.get('USN') and request.POST.get('Email_id') and request.POST.get('Phone_number') and request.POST.get('Event_name'):
            saverecord=Student()
            saverecord.Student_name= request.POST.get('Student_name')
            saverecord.USN= request.POST.get('USN')
            saverecord.Email_id= request.POST.get('Email_id')
            saverecord.Phone_number= request.POST.get('Phone_number')
            saverecord.Event_name= request.POST.get('Event_name')
            saverecord.save()
            messages.success(request,'registration successfull')
            return render(request,'Std_form.html')
    else:
            return render(request,'Std_form.html')

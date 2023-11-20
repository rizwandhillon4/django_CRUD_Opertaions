from django.shortcuts import render
from .models import User
from .forms import StudentRegistration
# Create your views here.

def add_show(request):

    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if  fm.is_valid():
      
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg =User(name=nm, email=em, password=pw,)
    
        reg.save()
        fm = StudentRegistration()
    else:
        fm = StudentRegistration()
        stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', context={'form':fm, 'stu':stud})

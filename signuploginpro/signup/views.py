from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm,LoginForm
from .models import SignupData

def Signup(request):
    form = RegistrationForm(request.POST or None)
    context = {
        'form' : form
    }

    if form.is_valid():
        print(form.cleaned_data)

        firstname = form.cleaned_data.get('firstname')
        lastname = form.cleaned_data.get('lastname')
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password1 = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')
        mobile = form.cleaned_data.get('mobile')

        data = SignupData(
            firstname=firstname,
            lastname=lastname,
            username=username,
            email=email,
            password1=password1,
            password2=password2,
            mobile=mobile
        )
        data.save()

    return render(request,'home.html' , context)
def Login(request):
    if request.method=="POST":
        lform=LoginForm(request.POST)
        if lform.is_valid():
            username=request.POST.get('username')
            password1=request.POST.get('password1')
            username=SignupData.objects.filter(username=username)
            password1=SignupData.objects.filter(password1=password1)
            if username and password1:
                return render(request, 'home1.html')

                # return HttpResponse("Login Successful")

            else:
                return HttpResponse("Enter a vaild data")
        else:
            return HttpResponse("User Invalid Data")
    else:
        lform=LoginForm()
        return render(request,'login.html',{'lform':lform})


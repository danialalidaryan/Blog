from django.shortcuts import render, redirect, HttpResponse
from .forms import signupForm
from .models import EmailAddress
from django.contrib.auth import authenticate, login, logout
from .models import CustomeUser


def userProfile(request, pk):
    return render(request, "Accounting/Profile.html", context={
        "user": CustomeUser.objects.all().get(UserName=pk)
    })


def signup_View(request):
    if request.user.is_authenticated:
        return redirect("Base:home")

    if request.method == "POST":
        form = signupForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            Email = EmailAddress.objects.create(User=None, Email=form.cleaned_data['temp_email'], Is_Default=True)
            user.Email = Email
            user.set_password(form.cleaned_data['password1'])
            user.save()
            Email.User = user
            Email.save()
            return redirect("Base:home")
        else:
            print(form.errors)
    else:
        form = signupForm()
    return render(request, "registration/signup.html", context={"form": form})


def signin_View(request):
    if request.user.is_authenticated:
        return redirect("Base:home")

    error = None

    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("Base:home")
        else:
            error = "نام کاربری یا رمز ورود اشتباه میباشد"

    return render(request, 'registration/signin.html', context={
        "Error":error,
    })


def signout_View(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("Base:home")
    else:
        return redirect("Base:home")

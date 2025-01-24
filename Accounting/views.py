from django.shortcuts import render, redirect, HttpResponse
from .forms import signupForm
# def userProfile(request, slug):
#     return render(request, "Accounting/userProfile.html", context={
#         "user": Profile.objects.all().filter(slug=slug)[0]
#     })

def signup_View(request):
    if request.method == "POST":
        pass
    else :
        form = signupForm()
    return render(request, "registration/signup.html", context={"form":form})

def signin_View(request):
    return render(request, "registration/signin.html", context={})

def test(request):
    if request.method =="POST":
        form = signupForm(request.POST)
        if form.is_valid() :
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return HttpResponse("Successful")
    else:
        form = signupForm()
    return render(request, "registration/signup.html", context={"form":form})


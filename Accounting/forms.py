from django.contrib.auth.forms import UserCreationForm
from .models import CustomeUser, Religion
from django import forms


class signupForm(UserCreationForm):
    class Meta:
        model = CustomeUser
        fields = [
            'UserName',
            "FirstName",
            "LastName",
            "NationalCode",
            "temp_email",
            'BirthDate',
            'Image',
            'password1',
            'password2',
            'About',
            "Gender",
            'Religion',
        ]
    UserName = forms.CharField(label="zmdi zmdi-account material-icons-name",required=True,widget=forms.TextInput(attrs={"name": "UserName", "id": "username", "placeholder": "Enter Your User Name"}))
    FirstName = forms.CharField(label="zmdi zmdi-account material-icons-name",required=True,widget=forms.TextInput(attrs={"name": "FirstName", "id": "firstname", "placeholder": "Enter Your First Name"}))
    LastName = forms.CharField(label="zmdi zmdi-account material-icons-name",required=True,widget=forms.TextInput(attrs={"name": "LastName", "id": "lastname", "placeholder": "Enter Your Last Name"}))
    NationalCode = forms.CharField(label="zmdi zmdi-account material-icons-name",required=True,widget=forms.TextInput(attrs={"name": "NationalCode", "id": "nationalcode", "placeholder": "Enter Your National Code"}))


    temp_email = forms.EmailField(label="zmdi zmdi-email",required=True,widget=forms.EmailInput(attrs={"name": "temp_email", "id": "temp_email", "placeholder": "Enter Your Emσil Address"}))
    BirthDate = forms.DateTimeField(label="zmdi zmdi-account-calendar",required=False,widget=forms.DateTimeInput(attrs={"name": "BirthDate", "id": "BirthDate", "placeholder": "Enter Your Birth Date"}))
    Image = forms.ImageField(label="zmdi zmdi-image",required=False)
    password1 = forms.CharField(label="zmdi zmdi-lock",required=True,widget=forms.TextInput(attrs={"name": "password1", "id": "password1", "placeholder": "Enter Your Password"}))
    password2 = forms.CharField(label="zmdi zmdi-lock-outline",required=True,widget=forms.TextInput(attrs={"name": "password2", "id": "password2", "placeholder": "Repeat Your Password"}))
    About = forms.CharField(max_length=500,required=False,widget=forms.Textarea(attrs={"name": "About", "id": "About", "class":"form-control", "rows":5, "cols":47, "placeholder": "Tell about yourself"}))



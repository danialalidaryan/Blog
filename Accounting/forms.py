from django.contrib.auth.forms import UserCreationForm
from .models import CustomeUser
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
        ]

    UserName = forms.CharField(label="zmdi zmdi-account material-icons-name", required=True, widget=forms.TextInput(
        attrs={"name": "UserName", "id": "username", "placeholder": "DanialSama"}),
                               help_text="Enter Your User Name. required")
    FirstName = forms.CharField(label="zmdi zmdi-account material-icons-name", required=True, widget=forms.TextInput(
        attrs={"name": "FirstName", "id": "firstname", "placeholder": "Danial"}),
                                help_text="Enter Your First Name. required")
    LastName = forms.CharField(label="zmdi zmdi-account material-icons-name", required=True, widget=forms.TextInput(
        attrs={"name": "LastName", "id": "lastname", "placeholder": "Alidaryan"}),
                               help_text="Enter Your Last Name. required")
    NationalCode = forms.CharField(label="zmdi zmdi-account material-icons-name", required=True, widget=forms.TextInput(
        attrs={"name": "NationalCode", "id": "nationalcode", "placeholder": "0150171080"}),
                                   help_text="Enter Your National Code. required")

    temp_email = forms.EmailField(label="zmdi zmdi-email", required=True, widget=forms.EmailInput(
        attrs={"name": "temp_email", "id": "temp_email", "placeholder": "danialalidaryangplay@gmail.com"}),
                                  help_text="Enter Your Emσil Address. required")
    BirthDate = forms.DateTimeField(label="zmdi zmdi-account-calendar", required=False, widget=forms.DateInput(
        attrs={'type': 'date', "name": "BirthDate", "id": "BirthDate"}), help_text="Enter Your Birth Date")
    Image = forms.ImageField(label="zmdi zmdi-image", required=False)
    password1 = forms.CharField(label="zmdi zmdi-lock", required=True,
                                widget=forms.PasswordInput(attrs={"name": "password1", "id": "password1"}),
                                help_text="Enter Your Password. required")
    password2 = forms.CharField(label="zmdi zmdi-lock-outline", required=True,
                                widget=forms.PasswordInput(attrs={"name": "password2", "id": "password2"}),
                                help_text="Repeat Your Password. required")
    About = forms.CharField(max_length=500, required=False, widget=forms.Textarea(
        attrs={"name": "About", "id": "About", "class": "form-control", "rows": 5, "cols": 47,
               "placeholder": "Tell about yourself"}))

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError("Passwords Are not the same.")

        return cleaned_data


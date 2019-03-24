from django import forms
from .models import Users

# class NewUser(forms.Form):
#     user_name   = forms.CharField(max_length = 200)
#     first_name  = forms.CharField(max_length = 200)
#     last_name   = forms.CharField(max_length = 200)
#     email_id    = forms.EmailField(max_length=50)
#     password    = forms.CharField(max_length=500)

class NewUser(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['user_name', 'first_name', 'last_name', 'email_id', 'password']
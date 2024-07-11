from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    # def __init__(self, *args, **kwargs):
    #     super(CustomUserCreationForm, self).__init__(self, *args, **kwargs)
    #     self.fields['username'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter Username...'})
    #     self.fields['password1'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter Password...'})
    #     self.fields['password2'].widget.attrs.update({'class':'form-control', 'placeholder':'Confirm Password...'})

        # Here we are Customizing ModelForm for applying css in ModelForm
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter Username'})
        self.fields['password1'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter Password'})
        self.fields['password2'].widget.attrs.update({'class':'form-control', 'placeholder':'Cofirm Password'})

        # for key, value in self.fields.items():
        #     value.widget.attrs.update({'class':'form-control', 'placeholder':'Confirm Password...'})
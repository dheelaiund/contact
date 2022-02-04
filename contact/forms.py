from django import forms
from .models import UserContactModel


class UserContactForm(forms.ModelForm):

    class Meta():
        model = UserContactModel
        exclude = ('user',)
        

    def __init__(self, *args, **kwargs):
        super(UserContactForm, self).__init__(*args, **kwargs)

        self.fields['firstname'].widget.attrs={
            'id': 'firstname',
            'class': 'form-control',
            'name': 'firstname', 
        }

        self.fields['lastname'].widget.attrs={
            'id': 'lastname',
            'class': 'form-control',
            'name': 'lastname', 
        }

        self.fields['nickname'].widget.attrs={
            'id': 'nickname',
            'class': 'form-control',
            'name': 'nickname', 
        }

        self.fields['gender'].widget.attrs={
            'id': 'gender',
            'class': 'form-control',
            'name': 'gender', 
        }

        self.fields['address'].widget.attrs={
            'id': 'address',
            'class': 'form-control',
            'name': 'address', 
        }

        self.fields['phone_number'].widget.attrs={
            'id': 'phone_number',
            'class': 'form-control',
            'name': 'phone_number', 
        }
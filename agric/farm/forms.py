from dataclasses import field
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import transaction
from .models import *


class FarmerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
    '''
    def save(self):
        user = super().save(commit=False)
        user.is_farmer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        farmer =  Farmer.objects.create(user=user)
        farmer.phone_number = self.cleaned_data.get('phone_number')
        farmer.save()
        
        return user
        '''


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from .models import Asset, Tenant, Owner

class NewUserForm(ModelForm):

  class Meta:
    model = Owner
    exclude = ['owner_asset']
    
class NewAssetForm(ModelForm):

  class Meta:
    model = Asset
    exclude = ['asset_owner']

  
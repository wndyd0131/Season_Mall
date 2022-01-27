from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()
class UserForm(UserCreationForm):
  # def __init__(self, *args, **kwargs):
  #   super().__init__(*args, **kwargs)
  #   self.fields['first_name'].required=True
  #   self.fields['last_name'].required=True
  #   self.fields['username'].required=True
  #   self.fields['email'].required=True
  
  class Meta:
    model = User
    fields = ['identifier', 'name', 'email', 'date_of_birth', 'bio', 'image']
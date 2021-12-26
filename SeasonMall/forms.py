from django import forms
from SeasonMall.models import Product

class AdditionForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = ['name', 'price', 'content']
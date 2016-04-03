from django import forms
from .models import Restaurant

class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = ('name','address','phone_number','price','rating', 'image','createdAt',)

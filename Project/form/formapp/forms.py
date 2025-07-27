from django import forms
from .models import format



class f_form(forms.ModelForm):
    class Meta:
        model = format
        fields = '__all__'
        widgets = {
            'first_Name': forms.TextInput(attrs={
                'placeholder': 'First Name', 'class': 'input-box'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name', 'class': 'input-box'
            }),
            'father_name': forms.TextInput(attrs={'placeholder':'Father name','class': 'input-box'}),
            'mother_name': forms.TextInput(attrs={
                'placeholder': 'Mother name', 'class': 'input-box'
            }),
            'dob': forms.TextInput(attrs={
                'placeholder': 'Date of birth','type':'date', 'class': 'input-box'
            }),
            'address': forms.TextInput(attrs={'placeholder': 'address','class': 'input-box'}),
            'phone' :forms.TextInput(attrs={'placeholder': 'phone','class' :'input-box' }),
        }

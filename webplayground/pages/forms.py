from django import forms
from .models import Page


class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title','content','order']
        #con attrs={'class':'form-control'} llamamos a la clase css de bootstrap
        #'content':forms.Textarea(attrs={'class':'form-control'}), no funcionaria porque tenemos un campo ckeditor
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'TITULO'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'order':forms.NumberInput(attrs={'class':'form-control'}),
        }
        labels = {
            'title':'',
            'content':'',
            'order':'',
        }

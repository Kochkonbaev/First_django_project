from django import forms
from .models import News


class NewForm(forms.ModelForm):
    
    class Meta:
        model = News
        fields = ('title', 'text', 'img')


        widgets = {
                'title': forms.TextInput(attrs={'class':'form-control'}),
                'text': forms.Textarea(attrs={'class':'form-control'}),
                'img': forms.URLInput(attrs={'class':'form-control'}),
                }
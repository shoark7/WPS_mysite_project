from django import forms
from member.models import MyUser

class AlbumForm(forms.Form):
    title = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control'}
        )
    )

class PhotoForm(forms.Form):
    title = forms.CharField(
        max_length=30,
        error_messages={'required': "Please enter photo's name."},
        widget=forms.TextInput(
            attrs={'class': 'form-control'},
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control'},
        )
    )
    img = forms.ImageField()



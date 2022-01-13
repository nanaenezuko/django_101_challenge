from django import forms

class PostPhotoForm(forms.Form):
    title = forms.CharField(max_length=100)
    caption = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
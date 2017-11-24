from django import forms

class CreateComment(forms.Form):
    text = forms.CharField(label='Your comment',max_length=30)

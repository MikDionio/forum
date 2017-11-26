from django import forms

class CreateComment(forms.Form):
    text = forms.CharField(label='Your comment',max_length=30)

class CreatePost(forms.Form):
    title = forms.CharField(label='Title: ', max_length = 50)
    content = forms.CharField(label = 'Content: ',max_length=1000)

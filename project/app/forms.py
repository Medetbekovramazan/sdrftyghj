from django import forms

class UserForm(forms.Form):
    name = forms.CharField(required=True, label='Имя', help_text='help_me')
    age = forms.IntegerField()
    email = forms.EmailField(required=False)
    required_css_class = 'myclass'

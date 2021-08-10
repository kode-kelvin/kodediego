from django import forms

class  ContactForm(forms.Form):

    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}
    ), required=True, max_length=50)
    subject = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Subject'}
    ), required=True, max_length=50)
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Message'}
    ), required=True)
    
from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
    email_address = forms.EmailField()
    subject = forms.CharField(label="email subject", max_length=100)
    email_body = forms.CharField(widget=forms.Textarea())
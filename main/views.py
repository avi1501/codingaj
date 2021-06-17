from django.shortcuts import render

from django.views import View
from django.http import HttpResponse

from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

class about(View):
    def get(self, request):
        context = {}
        return render(request, 'about.html', context )
    
class contact(View):
    def get(self, request):
        form = ContactForm()
        context = {
            'form':form,
            'post':True
        }
        return render(request, "contact.html", context)
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            # last_name = form.cleaned_data["last_name"]
            # subject=form.cleaned_data['subject']
            # message=form.cleaned_data['email_body']
            # sender = form.cleaned_data['email_address']
            # recipients = ['officiaaviid@gmail.com']
            # send_mail(subject, message, sender, recipients)
            context = {
                'post':False,
            }
            return render(request, "contact.html", context)
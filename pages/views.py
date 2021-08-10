from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.contrib import  messages
from django.http import HttpResponse
from .models import Project, Tag
from .forms import ContactForm
from django.conf import settings
from django.views.generic import  ListView



# Create your views here.

# home view
def home (request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'pages/index.html', context)







# details
def detail(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    context =  {
        'project':projectObj,
        'tags':tags
    }

    return render(request, 'pages/detail.html', context)


# about me

def about(request):

    return render(request, 'pages/about.html')


# contact

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            emailTo = [settings.EMAIL_HOST_USER]
            try:
                send_mail(email, message, subject, emailTo)
                return render(request, 'pages/success.html')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('.')
    return render(request, 'pages/contactme.html', {'form': form})









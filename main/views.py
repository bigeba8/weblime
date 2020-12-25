from django.shortcuts import render, redirect
from blog.models import Post
from django.http import HttpResponse
from django.contrib import messages
from main.forms import getInTouchForm
from django.core.mail import send_mail

# Create your views here.

def home(request):
    posts = Post.objects.filter().order_by('-date_posted')[0:3]
    return render(request, 'home.html', {'posts': posts, 'title': 'Digital Transformation'})


def who_we_are(request):
    return render(request, 'who-we-are.html', {'title': 'Who We Are'})


def solutions(request):
    return render(request, 'solutions.html', {'title': 'Solutions'})


def get_in_touch(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = getInTouchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            subject = "Website Inquiry"
            sender_email = 'support@WebLime.com'
            recipients = ['bigeba8@gmail.com']
            body = {
			'fullname': form.cleaned_data['fullname'],
			'email': form.cleaned_data['email'],
			'phone': form.cleaned_data['phone'],
			'message':form.cleaned_data['message']
			}

            message = "\n".join(body.values())

            #send send_mail
            send_mail(subject, message, sender_email, recipients)

            # redirect to a new URL:
            messages.success(request, f'Your form has been submited!')
            return redirect('home')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = getInTouchForm()

    return render(request, 'get-in-touch.html', {'form': form, 'title': 'Get In Touch'})

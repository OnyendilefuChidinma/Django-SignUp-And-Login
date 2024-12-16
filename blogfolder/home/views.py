from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import date
from .my_post import post

from .forms import ContactForm
from .models import ContactMessage
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.


# Getting all the dates in my post using obj key of 'date'
def get_post_date(post):
    return post['date']

def Bloghome(request):
    # return HttpResponse('welcome to my come')
    all_post = sorted(post, key=get_post_date, reverse=True)

    # print(all_post)
    return render(request, "blog/index.html", {
        "post_list": all_post[:2]
    })


def Post_list(request):
    return render(request, "blog/post.html")


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # pass
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            # Save data to the database
            contact_message = ContactMessage(name=name, email=email, phone=phone, message=message)
            contact_message.save()

            # Send email to admin
            admin_email = 'conyendilefu@gmail.com'
            subject_admin = f"New Contact Form Submission from {name}"
            message_to_admin = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
            send_mail(subject_admin, message_to_admin, email, [admin_email])

            # Send confirmation email to the user
            subject_user = "Thank you for contacting us"
            message_user = f"Dear {name},\n\nThank you for reaching out. We have received your message and will respond soon.\n\nBest regards,\nAtoZ company"
            send_mail(subject_user, message_user, 'conyendilefu@gmail.com', [email])

            return redirect('contact_success')  # Redirect to a success page
            # return redirect('contactus')  # Redirect to the same page

            # return redirect('success')  # Redirect to a success page
    else:
        form = ContactForm()
        print("Email not sent")

    return render(request, 'contact.html', {'form': form})


def contact_success(request):
    return HttpResponse('Success!')
    # return render(request,'success.html')


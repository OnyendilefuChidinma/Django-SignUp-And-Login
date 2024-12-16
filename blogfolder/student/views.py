from email import message
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import Student, CohortGroup, Student_profile, Program
from django .views.decorators.csrf import csrf_protect

# Create your views here.


def send_message(request):
    if request.method == 'POST':
        recipient_email = request.POST.get('student_email')
        sender_email = request.POST.get('sender_email')
        sender_phone = request.POST.get('sender_phone')
        subject = request.POST.get('message_subject')
        message_body = request.POST.get('message_body')

        previous_url = request.META.get("HTTP_REFERER", "student_profile")

        if sender_email and sender_phone and subject and message_body:
            try:
                send_mail(
                    subject=subject,
                    message=message_body,
                    from_email=sender_email,
                    recipient_list = [recipient_email],
                    fail_silently=False
                )
                messages.success(request, "Message sent successfully.")
                return redirect(previous_url)
                
            except Exception as e:
                messages.error(request, f"Error: {e}")
                return redirect(previous_url)

    print(sender_email, sender_phone, subject, message_body)



# def signup(request):
#     return render(request, 'auth/signup.html')
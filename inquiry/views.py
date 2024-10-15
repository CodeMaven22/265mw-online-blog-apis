from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .models import ContactInquiry
from .serializers import ContactInquirySerializer
from django.core.mail import send_mail
from django.conf import settings


class ContactInquiryCreateView(generics.CreateAPIView):
    queryset = ContactInquiry.objects.all()
    serializer_class = ContactInquirySerializer


# Example of how to send an email within a Django view
def send_test_email(request):
    send_mail(
        'Test Subject',  # Subject of the email
        'This is a test email message.',  # Message body
        settings.EMAIL_HOST_USER,  # Sender email
        [settings.ADMIN_EMAIL],  # Recipient list (your admin email)
        fail_silently=False,
    )
    return HttpResponse('Email sent successfully')

from rest_framework import serializers
from .models import ContactInquiry
from django.conf import settings
from django.core.mail import send_mail


class ContactInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInquiry
        fields = ['id', 'name', 'email', 'subject', 'message', 'created_at']
        read_only_fields = ['id', 'created_at']


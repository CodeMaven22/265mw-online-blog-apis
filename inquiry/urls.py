from django.urls import path
from .views import ContactInquiryCreateView

urlpatterns = [
    path('contact/', ContactInquiryCreateView.as_view(), name='contact-create'),
]

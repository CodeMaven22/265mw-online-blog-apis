from django.db import models
from django.conf import settings
from django.core.mail import send_mail


class ContactInquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    def save(self, *args, **kwargs):
        # Call the original save method
        super().save(*args, **kwargs)
        # Send email to the admin
        self.send_inquiry_email()

    def send_inquiry_email(self):
        subject = f"265mw-online Inquiry: {self.subject}"
        message_body = f"""
        \nYou have received a new contact inquiry from {self.name} ({self.email}).
        \nTitle: {self.subject} 
        \n{self.message}
        """
        message_body += "\nThis message was sent from your website."

        recipient_list = [admin_email for admin_email in settings.ADMIN_EMAIL]

        # Sending the email
        send_mail(
            subject,
            message_body,
            settings.DEFAULT_FROM_EMAIL,
            recipient_list,
            fail_silently=False,
        )

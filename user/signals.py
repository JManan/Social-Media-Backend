from django.contrib.auth.models import User
from app.models import PostList
from .models import Profile
from django.dispatch import receiver 
from django.db.models.signals import post_save
from sendgrid.helpers.mail import Mail, From, To, PlainTextContent, HtmlContent
from sendgrid import SendGridAPIClient
from decouple import config
from sendgrid.helpers.mail import Mail


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created and not kwargs.get('raw', False):
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# @reciever

@receiver(post_save, sender=PostList)
def send_email(sender, instance, **kwargs):
    sendgrid_client = SendGridAPIClient(config('SENDGRID_API_KEY'))
    from_email = From('f20212458@pilani.bits-pilani.ac.in')
    print(instance.author.email)
    l = []
    for receivers in instance.author.profile.email_receivers.all():
        l.append(To(receivers.email))
    print(l)
    if len(l) != 0:
        to_email = l
        subject = 'New Blog Posted'
        plain_text_content = PlainTextContent(
        "check out this new blog!!" 
        )
        html_content = HtmlContent(
            '<strong>instance.author "posted a new blog"</strong>'
        )
        message = Mail(from_email, to_email, subject, plain_text_content, html_content)
        print(message)
        sendgrid_client.send(message=message)



# @receiver(post_save, sender=Profile)
# def add_email_receiver(sender, instance, created, **kwargs):
#     if created and not kwargs.get('raw', False):
#         Profile.objects.create(email_receiver=instance)

# @receiver(post_save, sender=Profile)
# def remove_email_receiver(sender, instance, **kwargs):
#     instance.profile.save()

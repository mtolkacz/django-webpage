from celery import shared_task
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .models import Entry
from ..accounts.models import CustomUser


@shared_task
def latest_blog_entry_notification():

    latest = Entry.latest.all()

    if not latest:
        return

    active_users = CustomUser.objects.values('first_name', 'email').filter(is_active=True)

    if not active_users:
        return

    from_email = settings.EMAIL_HOST_USER
    latest_context = []
    for entry in latest:
        latest_context.append(
            {
                'title': entry.title,
                'url': entry.get_absolute_url(),
            }
        )
    domain = Site.objects.values_list('domain', flat=True).first()

    for entry in latest_context:
        for user in active_users:
            context = {
                'domain': domain,
                'first_name': user['first_name'],
                'title': entry['title'],
                'url': entry['url']
            }
            subject = f"Webpage: {entry['title']} - New blog entry available"
            message = render_to_string('blog/latest.html', context)
            send_mail(subject, message, from_email, [user['email']])


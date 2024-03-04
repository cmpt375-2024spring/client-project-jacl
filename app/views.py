from django.shortcuts import render
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.core.mail import send_mail, get_connection
from django.urls import reverse_lazy
import ssl 
import certifi
#print(certifi.where())
ssl_ca_certificates = '/Users/chahana/Desktop/client-project-jacl/venv/lib/python3.12/site-packages/certifi/cacert.pem'
ssl_context = ssl.create_default_context(cafile=ssl_ca_certificates)
from django.http import HttpResponse

# Create your views here.
pages = {
    'About Us': {
        'Mission & Vision': 'mission',
        'Board Members': 'board',
        'Activism': 'activism',
        'Cultural Programming': 'cultural_programming',
    },
    'Get Involved': {
        'Join SLC JACL': 'join',
        'Volunteer': 'volunteer',
        'Events': 'events',
    },
    'Resources': {
        'JACL Scholarships': 'scholarships',
        'Japanese Cultural Organizations': 'orgs/japanese',
        'Religious Oragnizations': 'orgs/religious',
        'AANHPI Organizations': 'orgs/aanhpi',
        'LGBTQIA+ Organizations': 'orgs/lgbtqiap'
    },
    'Contact': ''
}

context = { 'pages' : pages }

def index(request):
    context['active'] = ''
    return render(request, 'app/index.html', context)

class CustomPasswordResetView(PasswordResetView):
    def form_valid(self, form):
        email = form.cleaned_data['email']

        email_connection = get_connection(backend=None, fail_silently=False)

        # try:
        print("STARTING THE EMAIL PROCESS")
        print(send_mail(
            'Password Reset Request',
            'You have requested a password reset for your account.',
            'chahanadahal2002@gmail.com',  
            [email],
            connection=email_connection
        ))
        print("EMAIL HAS BEEN SENT SUCCESSFULLY")
        # except Exception as e : 
        #     print(e)
        return super().form_valid(form)

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('password_reset_complete')

def testemail(request):
    subject = 'Test email'
    message = 'This is a test email sent from Django.'
    from_email = 'chahanadahal1@gmail.com'
    recipient_list = ['chahanadahal1@gmail.com']  

    try:
        send_mail(subject, message, from_email, recipient_list)
        return HttpResponse('Test email sent successfully!')
    except Exception as e:
        return HttpResponse(f'Failed to send test email: {e}')
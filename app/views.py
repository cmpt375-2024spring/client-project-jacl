from django.shortcuts import render

# Create your views here.
pages = {
    '/': 'Home',
    'about': 'About',
    'events': 'Events',
    'membership': 'Membership',
    'programs': 'Programs',
}

context = { 'pages' : pages }

def index(request):
    context['active'] = '/'
    return render(request, 'index.html', context)
from django.shortcuts import render

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
    return render(request, 'index.html', context)
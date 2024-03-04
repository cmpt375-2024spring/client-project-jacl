from django.shortcuts import render

# Create your views here.
pages = {
    'About Us': {
        'Mission & Vision': 'mission',
        'Board Members': 'board',
        'History': 'history',
    },
    'Events': '',
    'Get Involved': {
        'Join SLC JACL': 'join',
        'Volunteer': 'volunteer',
    },
    'Resources': {
        'JACL Scholarships': 'scholarships',
        'Affiliates': 'affiliates'
    },
}

context = { 'pages' : pages }

def index(request):
    context['active'] = ''
    return render(request, 'app/index.html', context)


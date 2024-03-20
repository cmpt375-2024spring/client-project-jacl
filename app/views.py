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
    # SEND IN CONTEXT:
    # File names of slideshow images from database
    # Event list from database along with the file name of images
    context['active'] = ''
    return render(request, 'app/index.html', context)

def mission(request):
    context['active'] = 'mission'
    return render(request, 'app/mission.html', context)

def board(request):
    context['active'] = 'board'
    return render(request, 'app/board.html', context)

def history(request):
    context['active'] = 'history'
    return render(request, 'app/history.html', context)

def events(request):
    context['active'] = 'events'
    return render(request, 'app/events.html', context)

def join(request):
    context['active'] = 'join'
    return render(request, 'app/join.html', context)

def volunteer(request):
    context['active'] = 'volunteer'
    return render(request, 'app/volunteer.html', context)

def scholarships(request):
    context['active'] = 'scholarships'
    return render(request, 'app/scholarships.html', context)

def affiliates(request):
    context['active'] = 'affiliates'
    return render(request, 'app/affiliates.html', context)

def contact(request):
    context['active'] = 'contact'
    return render(request, 'app/contact.html', context)
from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User

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
    board_members = BoardMember.objects.all().values()
    return_board_members = []
    for members in board_members:
        member_details = {}
        #print(User.objects.all().values('username').filter(pk=members))
        userData = list(User.objects.all().filter(pk= members['user_id']).values())[0]
        member_details['name'] = userData['first_name'] + " " + userData['last_name']
        member_details['bio'] = members['bio']
        member_details['profile_picture'] = "user_upload/" + members['profile_picture'].split("/")[-2] + "/"  + members['profile_picture'].split("/")[-1]
        return_board_members.append(member_details)
    
    # print(return_board_members)

    context['board_members'] = return_board_members
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
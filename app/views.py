import datetime
from django.shortcuts import render
from .models import *
import json

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
    allEvents = Event.objects.all().values()
    # upcomingFiveEvents = Event.objects.all().filter(start_date__gte=datetime.date.today()).values()[:5]
    returnAllEvents = []
    for index,event in enumerate(allEvents):
        eventDetails = {}
        eventDetails['title'] = event['title']
        eventDetails['description'] = event['description']
        eventDetails['location'] = event['location']
        eventDetails['registration_link'] = event['registration_link']
        eventDetails['banner_image'] = "user_upload/" + event['banner_image'].split("/")[-2] + '/' + event['banner_image'].split("/")[-1]
        if(event['start_time'] and event['end_time']):
            eventDetails['start'] = event['start_date'].strftime("%Y-%m-%d") + "T" + event['start_time'].strftime("%H:%M:%S")
            eventDetails['end'] = event['end_date'].strftime("%Y-%m-%d") + "T" + event['end_time'].strftime("%H:%M:%S")
            eventDetails['allDay'] = False
        else:
            eventDetails['start'] = event['start_date'].strftime("%Y-%m-%d")
            eventDetails['end'] = event['end_date'].strftime("%Y-%m-%d")
            eventDetails['allDay'] = True

        returnAllEvents.append(eventDetails)

    context['allEvents'] = json.dumps(returnAllEvents)
    # print(returnAllEvents)
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
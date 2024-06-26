import datetime
from django.contrib import messages
from django.shortcuts import redirect, render

from app.forms import ContactModelForm
from .models import *
import json
from django.contrib.auth.models import User

pages = {
    'About Us': {
        'Mission & Vision': 'mission',
        'Board Members': 'board',
        'History': ['EXTERNAL','/pacificcitizen.org/did-you-know-everything-about-ja-history-in-utah/'],
    },
    'Events': None,
    'Statements': None,
    'Get Involved': {
        'Join SLC JACL': 'join',
        'Contact Us': 'contact',
    },
    'Resources': {
        'JACL Scholarships': ['EXTERNAL','/jacl.org/scholarships'],
        'Affiliates': 'affiliates'
    },
}

context = {'pages': pages}


def index(request):
    # SEND IN CONTEXT:
    # File names of slideshow images from database
    # Event list from database along with the file name of images
    images = HomePageImage.objects.all().values()
    finalImages = []
    for image in images:
        imageObj = {}
        imageObj['title'] = image['title']
        imageObj['image'] = "user_upload/" + image['image'].split("/")[-2] + '/' + image['image'].split("/")[-1]
        finalImages.append(imageObj)
    home_page_events = Event.objects.all().filter(start_date__gte=datetime.date.today()).values()
    finalEvents = []
    for event in home_page_events:
        eventObject = {}
        eventObject['title'] = event['title']
        eventObject['banner_image'] = "user_upload/" + event['banner_image'].split("/")[-2] + '/' + \
                                      event['banner_image'].split("/")[-1]
        finalEvents.append(eventObject)
    context['active'] = ''
    context['images'] = finalImages
    context['events'] = finalEvents
    return render(request, 'app/index.html', context)


def mission(request):
    missionVision = MissionVisionStatement.objects.all().values()
    for mission_vision in missionVision:
        context['mission'] = mission_vision['mission']
        context['vision'] = mission_vision['vision']

    context['active'] = 'mission'
    return render(request, 'app/mission.html', context)


def board(request):
    all_positions = ['', 'PRESIDENT', 'TREASURER', 'SECRETARY', 'MEMBERSHIP', 'YOUTH REP',
                     'SALT LAKE BUDDHIST TEMPLE LIASON', 'MATSUMOTO LIASON', 'PEACH GARDEN LIASON', 'AT LARGE']
    context['active'] = 'board'
    board_members = BoardMember.objects.all().order_by('position').values()
    return_board_members = []
    for members in board_members:
        member_details = {}
        # print(User.objects.all().values('username').filter(pk=members))
        userData = list(User.objects.all().filter(pk=members['user_id']).values())[0]
        member_details['name'] = userData['first_name'] + " " + userData['last_name']
        member_details['bio'] = members['bio']
        if members['position'] is not None:
            member_details['position'] = all_positions[int(members['position'])]
        else:
            member_details['position'] = None
        if (members['profile_picture']):
            member_details['profile_picture'] = "user_upload/" + members['profile_picture'].split("/")[-2] + "/" + \
                                                members['profile_picture'].split("/")[-1]
        else:
            member_details['profile_picture'] = None

        return_board_members.append(member_details)

    # print(return_board_members)

    context['board_members'] = return_board_members
    return render(request, 'app/board.html', context)


def history(request):
    context['active'] = 'history'
    return render(request, 'app/history.html', context)


def events(request):
    context['active'] = 'events'
    allEvents = Event.objects.all().values()
    upcomingEvents = Event.objects.all().filter(start_date__gte=datetime.date.today()).values()
    arrayOfAllEvents = []
    arrayOfUpcomingEvents = []
    for event in allEvents:
        eventDetails = {}
        eventDetails['title'] = event['title']
        eventDetails['description'] = event['description']
        eventDetails['location'] = event['location']
        eventDetails['registration_link'] = event['registration_link']
        eventDetails['banner_image'] = "user_upload/" + event['banner_image'].split("/")[-2] + '/' + \
                                       event['banner_image'].split("/")[-1]
        if (event['start_time'] and event['end_time']):
            eventDetails['start'] = event['start_date'].strftime("%Y-%m-%d") + "T" + event['start_time'].strftime(
                "%H:%M:%S")
            eventDetails['end'] = event['end_date'].strftime("%Y-%m-%d") + "T" + event['end_time'].strftime("%H:%M:%S")
            eventDetails['allDay'] = False
        else:
            eventDetails['start'] = event['start_date'].strftime("%Y-%m-%d")
            eventDetails['end'] = event['end_date'].strftime("%Y-%m-%d")
            eventDetails['allDay'] = True

        arrayOfAllEvents.append(eventDetails)
    for event in upcomingEvents:
        eventDetails = {}
        eventDetails['title'] = event['title']
        eventDetails['description'] = event['description']
        eventDetails['location'] = event['location']
        eventDetails['registration_link'] = event['registration_link']
        eventDetails['banner_image'] = "user_upload/" + event['banner_image'].split("/")[-2] + '/' + \
                                       event['banner_image'].split("/")[-1]
        if (event['start_time'] and event['end_time']):
            eventDetails['start'] = event['start_date'].strftime("%b %d, %Y") + " - " + event['start_time'].strftime(
                "%-I:%M %p")
            eventDetails['end'] = event['end_date'].strftime("%b %d, %Y") + " - " + event['end_time'].strftime(
                "%-I:%M %p")
        else:
            eventDetails['start'] = event['start_date'].strftime("%b %d, %Y")
            eventDetails['end'] = event['end_date'].strftime("%b %d, %Y")

        arrayOfUpcomingEvents.append(eventDetails)

    context['upcomingEvents'] = arrayOfUpcomingEvents
    context['allEvents'] = json.dumps(arrayOfAllEvents)
    return render(request, 'app/events.html', context)


def join(request):
    context['active'] = 'join'
    joinus = JoinUs.objects.get()
    context['joinus'] = joinus
    return render(request, 'app/join.html', context)


def volunteer(request):
    context['active'] = 'volunteer'
    return render(request, 'app/volunteer.html', context)


def scholarships(request):
    context['active'] = 'scholarships'
    return render(request, 'app/scholarships.html', context)


def affiliates(request):
    japaneseAffiliates = Affiliate.objects.all().filter(group='Japanese Cultural Organizations').values()
    returnJapaneseAffiliates = []
    for japaneseAffiliate in japaneseAffiliates:
        japaneseAffiliatesObj = {}
        japaneseAffiliatesObj['name'] = japaneseAffiliate['name']
        japaneseAffiliatesObj['description'] = japaneseAffiliate['description']
        japaneseAffiliatesObj['website'] = japaneseAffiliate['website']
        returnJapaneseAffiliates.append(japaneseAffiliatesObj)

    religiousAffiliates = Affiliate.objects.all().filter(group='Religious Organizations').values()
    returnreligiousAffiliates = []
    for religiousAffiliate in religiousAffiliates:
        religiousAffiliatesObj = {}
        religiousAffiliatesObj['name'] = religiousAffiliate['name']
        religiousAffiliatesObj['description'] = religiousAffiliate['description']
        religiousAffiliatesObj['website'] = religiousAffiliate['website']
        returnreligiousAffiliates.append(religiousAffiliatesObj)

    aanphiAffiliates = Affiliate.objects.all().filter(group='AANHPI Organizations').values()
    returnaanphiAffiliates = []
    for aanphiAffiliate in aanphiAffiliates:
        aanphiAffiliatesObj = {}
        aanphiAffiliatesObj['name'] = aanphiAffiliate['name']
        aanphiAffiliatesObj['description'] = aanphiAffiliate['description']
        aanphiAffiliatesObj['website'] = aanphiAffiliate['website']
        returnaanphiAffiliates.append(aanphiAffiliatesObj)
    
    lgbtqiaAffiliates = Affiliate.objects.all().filter(group='LGBTQIA+ Organizations').values()
    returnlgbtqiaAffiliates = []
    for lgbtqiaAffiliate in lgbtqiaAffiliates:
        lgbtqiaAffiliatesObj = {}
        lgbtqiaAffiliatesObj['name'] = lgbtqiaAffiliate['name']
        lgbtqiaAffiliatesObj['description'] = lgbtqiaAffiliate['description']
        lgbtqiaAffiliatesObj['website'] = lgbtqiaAffiliate['website']
        returnlgbtqiaAffiliates.append(lgbtqiaAffiliatesObj)
    
    otherAffiliates = Affiliate.objects.all().filter(group='Other Affiliates').values()
    returnotherAffiliates = []
    for otherAffiliate in otherAffiliates:
        otherAffiliatesObj = {}
        otherAffiliatesObj['name'] = otherAffiliate['name']
        otherAffiliatesObj['description'] = otherAffiliate['description']
        otherAffiliatesObj['website'] = otherAffiliate['website']
        returnotherAffiliates.append(otherAffiliatesObj)

    context['japaneseAffiliates'] = returnJapaneseAffiliates
    context['religiousAffiliates'] = returnreligiousAffiliates
    context['aanphiAffiliates'] = returnaanphiAffiliates
    context['lgbtqiaAffiliates'] = returnlgbtqiaAffiliates
    context['otherAffiliates'] = returnotherAffiliates
    context['active'] = 'affiliates'
    return render(request, 'app/affiliates.html', context)


def contact(request):
    if(request.method == "POST"):
        inputs = ContactModelForm(request.POST)
        if inputs.is_valid():
            saving_values = Contact.objects.create(
                name = inputs.cleaned_data['name'],
                email = inputs.cleaned_data['email'],
                phone = inputs.cleaned_data['phone'],
                message = inputs.cleaned_data['message']
            )
            saving_values.save()
            messages.success(request, 'Successfully Sent Message')
        else:
            messages.error(request, 'Failed to Send Message')
        return redirect('contact')


    context['active'] = 'contact'
    context['form'] = ContactModelForm()
    return render(request, 'app/contact.html', context)

def statements(request):
    allStatements = Statement.objects.all().values()
    statements = []
    for statement in allStatements:
        statementInfo = {}
        statementInfo['id'] = statement['id']
        statementInfo['title'] = statement['title']
        statementInfo['slug'] = statement['title'].replace(" ", "_")
        statements.append(statementInfo)
    context['statements'] = statements
    context['active'] = 'statements'
    return render(request, 'app/statements.html', context)

def statement(request):
    statement_id = request.GET['statement_id']
    thisStatement = Statement.objects.all().filter(pk=statement_id).values()
    for statement in thisStatement:
        statementInfo = {}
        statementInfo['title'] = statement['title']
        statementInfo['description'] = statement['description']
        statementInfo['image'] = "user_upload/" + statement['image'].split("/")[-2] + '/' + \
                                 statement['image'].split("/")[-1]
    context['statement'] = statementInfo
    context['active'] = 'statement'
    return render(request, 'app/statement.html', context)

from django.shortcuts import render, redirect
from .forms import *
from .models import *


# Create your views here.
def index(request):
    return render(request, 'myProject/index.html')


def add(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = EventForm()
            return render(request, 'myProject/addData.html', {'Participants': form})
        else:
            participant = Participants.objects.get(pk=id)
            form = EventForm(instance=participant)
            return render(request, 'myProject/addData.html', {'Participants': form})
    else:
        if id == 0:
            form = EventForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('show')
        else:
            participant = Participants.objects.get(pk=id)
            form = EventForm(request.POST, instance=participant)
            if form.is_valid():
                form.save()
    return redirect('show')


def show(request):
    data = Participants.objects.all().order_by('-id')
    return render(request, 'myProject/show.html', context={'Participants': data})


def showEvent(request):
    Plan = Planner.objects.all()
    context = {'Events': Plan}
    if request.method == "POST":
        Event = Participants.objects.filter(Event_id=request.POST['Events'])
        context = {'Participants': Event, 'Events': Plan}
        return render(request, 'myProject/showEvent.html', context)

    return render(request, 'myProject/showEvent.html', context)


def showVenue(request):
    ven = Participants.objects.all()
    context = {'Venues': ven}
    if request.method == "POST":
        event = Participants.objects.filter(p_date=request.POST['date'])
        print(event)
        context = {'Participants': event, 'Venues': ven}

    return render(request, 'myProject/showVenue.html', context)


def AddEvents(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = AddEvent()
            return render(request, 'myProject/AddEvent.html', context={'Event': form})
        else:
            planners = Planner.objects.get(pk=id)
            form = AddEvent(instance=planners)
            return render(request, "myProject/AddEvent.html", context={'Event': form})
    else:
        if id == 0:
            form = AddEvent(request.POST)
            if form.is_valid():
                form.save()
            return redirect('ShowAllEvent')
        else:
            planners = Planner.objects.get(pk=id)
            form = AddEvent(request.POST, instance=planners)
            if form.is_valid():
                form.save()
    return redirect('ShowAllVenue')


def catalog(request):
    data = Planner.objects.all()
    return render(request, 'myProject/ShowAllEvent.html', context={'Planner': data})


def event_venue(request):
    values = Venue.objects.all()
    return render(request, 'myProject/ShowAllEvent.html', context={'Venue': values})


def delete(request, id):
    Participant = Participants.objects.get(pk=id)
    Participant.delete()
    return redirect('show')


def deleteevent(request, id):
    Planners = Planner.objects.get(pk=id)
    Planners.delete()
    return redirect('ShowAllEvent')


def delet_venue(request, id):
    variable = Venue.objects.get(pk=id)
    variable.delete()
    return redirect('ShowAllVenue')


def addVenue(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = AddVenue()
            return render(request, 'myProject/AddVenue.html', context={'Venue': form})
        else:
            venues = Venue.objects.get(pk=id)
            form = AddVenue(instance=venues)
            return render(request, "myProject/AddVenue.html", context={'Venue': form})
    else:
        if id == 0:
            form = AddVenue(request.POST)
            if form.is_valid():
                form.save()
            return redirect('addData')
        else:
            venues = Venue.objects.get(pk=id)
            form = AddVenue(request.POST, instance=venues)
            if form.is_valid():
                form.save()
    return redirect('addData')

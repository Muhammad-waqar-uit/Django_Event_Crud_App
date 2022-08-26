from django import forms
from .models import *
from .widget import *


class EventForm(forms.ModelForm):
    class Meta:
        model = Participants
        fields = ('p_name', 'email', 'p_contact', 'p_date', 'p_time', 'venue', 'Event_id')
        labels = {
            'p_name': 'Event Name',
            'email': 'Email Address',
            'p_contact': 'Contact No',
            'venue': 'Venue',
            'Event_id': 'Events'
        }
        widgets = {
            'p_date': DatePickerInput(),
            'p_time': TimePickerInput(),
        }


class AddVenue(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ('venues',)
        labels = {
            'venues': 'Venue'
        }


class AddEvent(forms.ModelForm):
    class Meta:
        model = Planner
        fields = ('Events',)
        labels = {
            'Events': 'Event Category'
        }

from django.db import models


# Create your models here.
class Planner(models.Model):
    Events = models.CharField(max_length=50)

    def __str__(self):
        return self.Events


class Venue(models.Model):
    venues = models.CharField(max_length=30)

    def __str__(self):
        return self.venues


class Participants(models.Model):
    p_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    p_contact = models.CharField(max_length=50)
    p_date = models.DateField("Date")
    p_time = models.TimeField("Time")
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    Event_id = models.ForeignKey(Planner, on_delete=models.CASCADE)

    def __str__(self):
        return self.p_name



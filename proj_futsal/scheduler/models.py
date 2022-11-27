# Create your models here.
from django.db import models
import datetime

class Event(models.Model):
    class EventStatus(models.TextChoices):
        CONFIRMED = 'CO', 'Confirmed'
        UNCONFIRMED = 'UC', 'Unconfirmed'
        CANCELLED = 'CA', 'Cancelled'
    event_name = models.CharField(max_length=200)
    event_date = models.DateField(default = datetime.datetime.today())
    event_start = models.TimeField(default = datetime.datetime.now())
    event_end = models.TimeField(default = datetime.datetime.now())
    event_created = models.DateTimeField(auto_now_add=True)
    event_updated = models.DateTimeField(auto_now=True)
    event_comment = models.TextField()
    event_status = models.CharField(max_length = 2, choices = EventStatus.choices)

    class Meta:
        ordering = ['event_date', 'event_start']
    def __str__(self):
        return self.event_name


class Player(models.Model):
    class PlayerStatus(models.TextChoices):
        PLAYER = 'PL', 'Player'
        WATCHING = 'WA', 'Watching'
    class AttendanceStatus(models.TextChoices):
        CONFIRMED = 'CO', 'Confirmed'
        MAYBE = 'MB', 'Maybe'
        WILL_NOT_ATTEND = 'NO', 'Will not attend'
    event = models.ForeignKey(Event, on_delete = models.CASCADE, related_name = 'relevant_event_name')
    name = models.CharField(max_length=200)
    player_status = models.CharField(max_length = 2, choices= PlayerStatus.choices)
    attendance_status = models.CharField(max_length = 2, choices= AttendanceStatus.choices)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    comment = models.TextField(null=True, blank=True)
    class Meta:
        ordering = ['created']
    def __str__(self):
        return self.name


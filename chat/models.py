from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)
    cnt_member = models.IntegerField(default = 0)
    create_time = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.label

class Message(models.Model):
    room = models.ForeignKey(Room, models.PROTECT, related_name='messages')
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    def __unicode__(self):
        return '[{timestamp}] {handle}: {message}'.format(**self.as_dict())

    @property
    def formatted_timestamp(self):
        return self.timestamp.strftime('%b %-d %-I:%M %p')

    def as_dict(self):
        return {'handle': self.handle, 'message': self.message, 'timestamp': self.formatted_timestamp}

class Mask(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    face = models.ImageField()
    area = models.CharField(max_length=50)
    descript = models.TextField()
    start = models.DateTimeField()

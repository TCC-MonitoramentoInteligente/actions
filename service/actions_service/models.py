from django.db import models


class Event(models.Model):
    event = models.CharField(max_length=50, null=False, blank=False, editable=False)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    contact = models.EmailField(null=False, blank=False, editable=False)
    camera = models.CharField(max_length=100, null=False, blank=False, editable=False)

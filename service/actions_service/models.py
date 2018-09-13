from django.db import models

GPU_SERVER_IP = '10.242.128.252'
event_print_url = 'http://{}:8000/object-detection/print/'.format(GPU_SERVER_IP)


class Event(models.Model):
    event = models.CharField(max_length=50, null=False, blank=False, editable=False)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    contact = models.EmailField(null=False, blank=False, editable=False)
    camera = models.CharField(max_length=100, null=False, blank=False, editable=False)
    result = models.TextField()

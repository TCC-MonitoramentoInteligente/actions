import paho.mqtt.client as mqtt
from django.db import models

from service import settings

event_print_url = 'http://{}:{}/object-detection/print/'\
    .format(settings.OBJECT_DETECTION_SERVICE_IP, settings.OBJECT_DETECTION_SERVICE_PORT)
camera_url = 'http://{}:{}/cameras/'\
    .format(settings.USERS_SERVICE_IP, settings.USERS_SERVICE_PORT)

mqtt_client = mqtt.Client()
mqtt_client.connect(settings.BROKER_IP)
mqtt_client.loop_start()


class Event(models.Model):
    event = models.CharField(max_length=50, null=False, blank=False, editable=False)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    contact = models.EmailField(null=False, blank=False, editable=False)
    camera = models.CharField(max_length=100, null=False, blank=False, editable=False)
    result = models.TextField()

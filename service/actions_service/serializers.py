from rest_framework import serializers

from actions_service.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'event', 'date', 'contact', 'camera', 'result')

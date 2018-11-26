import requests
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from actions_service.models import Event, event_print_url
from actions_service.serializers import EventSerializer

from email_service import send_email


def get_contact(camera):
    # TODO: get contact from camera id
    return 'eventos.mia@outlook.com'


@api_view(['GET', 'POST'])
def event(request):
    """
    List all Events, or create a new Event.
    """
    if request.method == 'GET':
        e = Event.objects.all()
        serializer = EventSerializer(e, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        try:
            event_name = request.POST['event']
            camera = request.POST['camera']
            contact = get_contact(camera)
            event_print = requests.get(url=event_print_url, params={'cam_id': camera})
            frame64 = event_print.text
            e = Event.objects.create(event=event_name, camera=camera, contact=contact)
            e.result = send_email(contact, event_name, e.date, camera, frame64)
            e.save()
            return Response(status=status.HTTP_200_OK)
        except KeyError as ex:
            Response(ex, status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Method not allowed", status=405)

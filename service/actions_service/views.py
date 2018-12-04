import requests
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from actions_service.models import Event, mqtt_client, event_print_url, camera_url
from actions_service.serializers import EventSerializer

from email_service import send_email


def get_contact():
    return 'eventos.mia@outlook.com'


@api_view(['GET', 'POST'])
def event(request):
    """
    List all Events, or create a new Event.
    """

    external_service_not_responding = 'Action error. Users service or Object detection service is not responding.'
    success = 'Action service. Event from camera {} was successfully processed'

    if request.method == 'GET':
        e = Event.objects.all()
        serializer = EventSerializer(e, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        try:
            event_name = request.POST['event']
            cam_id = request.POST['cam_id']
            contact = get_contact()
            event_print = requests.get(url=event_print_url, params={'cam_id': cam_id}, timeout=5)
            frame64 = event_print.text
            cam = requests.get(url=camera_url + '{}/'.format(cam_id), timeout=4).json()
            e = Event.objects.create(event=event_name, camera=cam_id, contact=contact)
            e.result = send_email(contact, event_name,
                                  cam['id'], cam['model_name'], cam['address'], frame64)
            e.save()
            mqtt_client.publish(topic="actions/logs/success",
                                payload=success.format(cam_id))
            return Response(status=status.HTTP_200_OK)
        except KeyError as ex:
            print(ex)
            Response(ex, status=status.HTTP_400_BAD_REQUEST)
        except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError) as ex:
            print(ex)
            mqtt_client.publish(topic="actions/logs/success",
                                payload=external_service_not_responding)
            Response(ex, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return HttpResponse("Method not allowed", status=405)

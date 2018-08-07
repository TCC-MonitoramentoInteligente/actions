from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from actions_service.models import Event
from actions_service.serializers import EventSerializer

from email_service import send_email


def get_contact(camera):
    # TODO: get contact from camera id
    contacts = ['one@example.com', 'two@example.com']
    if camera == '1':
        return contacts[0]
    elif camera == '2':
        return contacts[1]
    else:
        return 'null@email.com'


@api_view(['GET', 'POST'])
def event(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Event.objects.all()
        serializer = EventSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        try:
            event_name = request.POST['event']
            camera = request.POST['camera']
            contact = get_contact(camera)
            e = Event.objects.create(event=event_name, camera=camera, contact=contact)
            e.result = send_email(contact, event, e.date, camera)
            e.save()
            return Response(status=status.HTTP_200_OK)
        except KeyError as ex:
            Response(ex, status=status.HTTP_400_BAD_REQUEST)

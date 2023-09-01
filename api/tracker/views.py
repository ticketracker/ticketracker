from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status

from .serializers import TrackerSerializer

@api_view(["POST"])
def api_create_tracker(request):
    data = JSONParser().parse(request)
    serializer = TrackerSerializer(data=data)
    
    if serializer.is_valid():
        instance = serializer.save()
        return Response("Your tracker just created, this will send you ticket informations when tracks something")

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

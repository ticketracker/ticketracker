from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TrackerSerializer
from rest_framework.parsers import JSONParser


@api_view(["POST"])
def api_create_tracker(request):
    data = JSONParser().parse(request)
    serializer = TrackerSerializer(data=data)
    
    if serializer.is_valid():
        instance = serializer.save()
        return Response("OK")

    return Response(serializer.errors)
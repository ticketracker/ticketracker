from rest_framework import serializers
from .models import Tracker, TicketRequest
from .models import Provider


class PassengerSerializer(serializers.Serializer):
    adult = serializers.IntegerField()
    baby = serializers.IntegerField()
    child = serializers.IntegerField()


class TicketRequestSerializer(serializers.Serializer):
    vehicle = serializers.CharField()
    origin_city = serializers.CharField()
    destination_city = serializers.CharField()
    passengers = PassengerSerializer()
    departue_date = serializers.DateTimeField()
    price_from = serializers.IntegerField()
    price_to = serializers.IntegerField()
    time_start = serializers.TimeField()
    time_end = serializers.TimeField()
    return_date = serializers.DateTimeField(default=None)
    one_way = serializers.BooleanField(default=True)
    class_type = serializers.CharField(default=None)


class TrackerSerializer(serializers.Serializer):
    ticket_request = TicketRequestSerializer()
    active_duration = serializers.DurationField()
    delay_between_track = serializers.IntegerField()
    report_to = serializers.EmailField()
    providers = serializers.ListField(
        child=serializers.CharField()
    )

    def create(self, validated_data):
        ticket_request_data = validated_data.pop('ticket_request')
        ticket_request = TicketRequest(
            vehicle=ticket_request_data["vehicle"],
            origin_city=ticket_request_data["origin_city"],
            destination_city=ticket_request_data["destination_city"],
            passengers=ticket_request_data["passengers"],
            departue_date=ticket_request_data["departue_date"],
            price_from=ticket_request_data["price_from"],
            price_to=ticket_request_data["price_to"],
            time_start=ticket_request_data["time_start"],
            time_end=ticket_request_data["time_end"],
            return_date=ticket_request_data["return_date"],
            one_way=ticket_request_data["one_way"],
            class_type=ticket_request_data["class_type"],
        )
        ticket_request.save()

        providers = Provider.objects.filter(name__in=validated_data.pop('providers'))
        tracker = Tracker(ticket_request=ticket_request, **dict(validated_data))
        tracker.save()
        tracker.providers.set(providers)
        return tracker

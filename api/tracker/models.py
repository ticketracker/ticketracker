from django.db import models
from django.core.exceptions import ValidationError

def get_default_passengers():
    return {"adult": 1, "baby": 0, "child": 0}

class TicketRequest(models.Model):
    VEHICLES = [
        ('BUS', 'Bus'),
        ('TRAIN', 'Train'),
        ('AIRPLANE', 'Aairplane'),
        ('SHIP', 'Ship')
    ]

    vehicle = models.CharField(max_length=50, choices=VEHICLES)
    origin_city = models.CharField(max_length=50)
    destination_city = models.CharField(max_length=50)
    passengers = models.JSONField(default=get_default_passengers, help_text="for example: {\"adult\": 1, \"baby\": 0, \"child\": 0}")
    departue_date = models.DateTimeField()
    price_from = models.PositiveIntegerField()
    price_to = models.PositiveIntegerField()
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    return_date = models.DateTimeField(blank=True, null=True)
    one_way = models.BooleanField(default=True)
    class_type = models.CharField(max_length=50, blank=True, null=True)

    def clean(self, *args, **kwargs):
        if type(self.passengers) != dict:
            raise ValidationError("invalid value pass for passengers, only mapping/dict are valid")
        if 'baby' not in self.passengers or 'adult' not in self.passengers or 'child' not in self.passengers:
            raise ValidationError("fields 'adult', 'child', 'baby' is required in passengers")
        if type(self.passengers['baby']) != int or type(self.passengers['baby']) != int or type(self.passengers['baby']) != int: 
            raise ValidationError("values for passengers must be integer")
        if sum(self.passengers.values()) <= 0:
            raise ValidationError("please enter one passenger at least, count of passengers are not valid")
        return super().clean(*args, **kwargs)


class Provider(models.Model):
    name = models.CharField(max_length=124)


class Tracker(models.Model):
    tracker_id = models.UUIDField(unique=True, editable=False, blank=True)
    ticket_request = models.ForeignKey(TicketRequest, on_delete=models.CASCADE)
    providers = models.ManyToManyField(Provider)
    active_duration = models.DurationField()
    report_to = models.CharField(max_length=50)
    delay_between_track = models.IntegerField()
    active = models.BooleanField(default=True)
    result = models.TextField(blank=True)

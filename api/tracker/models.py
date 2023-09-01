from django.db import models


class TicketRequest(models.Model):
    vehicle = models.CharField(max_length=50)
    origin_city = models.CharField(max_length=50)
    destination_city = models.CharField(max_length=50)
    passengers = models.IntegerField()
    departue_date = models.DateTimeField()
    price_range = models.IntegerField()
    time_range = models.DateTimeField()
    return_date = models.DateTimeField()
    one_way = models.BooleanField()
    class_type = models.CharField(50)


class Tracker(models.Model):
    ticket_request = models.ForeignKey(TicketRequest, on_delete=models.CASCADE)
    providers = models.CharField(max_length=150)
    active_duration = models.DateTimeField()
    report_to = models.CharField(max_length=50)
    delay_between_track = models.IntegerField()
    active = models.BooleanField()
    result = models.TextField()
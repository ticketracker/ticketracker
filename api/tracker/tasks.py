import asyncio
import datetime

from core.tracker import Tracker
from core.ticket import TicketRequest
from core.provider import providers_list
from config.celery import app


async def create_tracker(data: dict):
	ticket_request = TicketRequest(
		vehicle=data['ticket_request']['vehicle'],
		origin_city=data['ticket_request']['origin_city'],
		destination_city=data['ticket_request']['destination_city'],
		passengers=data['ticket_request']['passengers'],
		departue_date=data['ticket_request']['departue_date'],
		price_range=data['ticket_request']['price_range'],
		time_range=data['ticket_request']['time_range'],
		return_date=data['ticket_request']['return_date'],
		one_way=data['ticket_request']['one_way'],
		class_type=data['ticket_request']['class_type'],
	)

	tracker = Tracker(
		ticket_request=ticket_request,
		active_duration=datetime.timedelta(seconds=data['active_duration']),
		delay_between_track=data['delay_between_track'],
		report_to=data['report_to'],
		providers={p:providers_list[p] for p in data['providers']},
	)
	if not tracker.active:
		return

	await tracker.start_tracking()
	print(tracker.result)




@app.task
def task_create_tracker(data: dict):
	asyncio.run(create_tracker(data))
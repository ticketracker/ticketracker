from typing import Optional
from dataclasses import dataclass, field
import uuid
import datetime
import json
import asyncio
import logging

from core.ticket import TicketRequest
from core.provider import Provider


MAX_DURATION = datetime.timedelta(days=7)
HOUR = datetime.timedelta(hours=1)
DEFAULT_DELAY = 60*60


@dataclass
class Tracker:
	id: Optional[uuid.uuid4] = field(init=False)
	ticket_request: TicketRequest
	providers: dict[Provider] | Provider = field(repr=False)
	active_duration: datetime.timedelta
	report_to: str
	delay_between_track: int = DEFAULT_DELAY
	active: bool = field(init=False, default=True)
	result: str = field(init=False)

	def __post_init__(self):
		self.id = uuid.uuid4()
		if self.active_duration > MAX_DURATION:
			logging.warning("activation duration cannot be more than one week")
			self.result = "error: activation duration is more than one week"
			self.active = False

		if self.active_duration > HOUR and self.delay_between_track < DEFAULT_DELAY:
			logging.error("Cannot create a tracker with more than one hour duration and less than one hour delay")
			self.result = "error: tracker has more than one-hour duration and less than one-hour delay"
			self.active = False

		if isinstance(self.providers, Provider):
			self.providers = {self.providers.name: self.providers}
		
		self.delay_between_track = min(self.delay_between_track, self.active_duration.total_seconds())

	async def start_tracking(self) -> None:
		"""Main code for start tracking tickets"""
		
		if not self.active:
			logging.error("Tracker with id %s is not activate", self.id)
			return

		til_time = datetime.datetime.now() + self.active_duration

		counter = int(self.active_duration.total_seconds() // self.delay_between_track)		
		for i in range(counter):
			tasks = [
				asyncio.create_task(self.track(provider))
				for name, provider in self.providers.items()
				if provider.support_vehicle(self.ticket_request.vehicle.upper())
			]
			if not tasks:
				self.active = False
				self.result = "error: there is no providers for intended ticket request"
				return

			results = await asyncio.gather(*tasks)
			if i != counter-1:
				# only await if there is something next, and don't if this is the last time
				await asyncio.sleep(self.delay_between_track)
		else:
			logging.info("Tracker with id %s just finished.", self.id)
			self.result = "done: tracker finished"
	
	async def track(self, provider: Provider) -> None:
		"""Track for each provider"""
		tickets = await provider.handler.search(self.ticket_request)
		logging.info("Tracker with id %s found %d intended tickets from %s provider", self.id, len(tickets) if tickets else 0, provider.name)
		return tickets

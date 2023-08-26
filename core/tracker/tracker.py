from typing import Optional
from dataclasses import dataclass, field
import uuid
import datetime

from core.ticket import TicketRequest
from core.provider import Provider


@dataclass
class Tracker:
	id : Optional[uuid.uuid4] = field(init=False)
	tickete_request: TicketRequest
	providers: list[Provider] = field(repr=False)
	active_duration: datetime.timedelta
	report_to: str


	def __post_init__(self):
		self.id = uuid.uuid4()

	def start_tracking(self) -> None:
		"""Main code for start tracking tickets"""
		# NOTE: this function make a event in background asynchronosly (maybe celery)
		# then for each provider make a search and tracking for each ticket. it tracked a ticket send it to the 
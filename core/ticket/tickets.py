from dataclasses import dataclass
import datetime


@dataclass
class TicketRequest:
	vehicle: 'Vehicle'
	origin_city: str
	destination_city: str
	passengers: dict
	departue_date: datetime.datetime
	price_range: tuple[int]
	time_range: tuple[datetime.time]
	return_data: datetime.datetime | None = None
	on_way: bool = True
	class_type: str | None = None


@dataclass
class Ticket:
	pass

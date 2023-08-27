from dataclasses import dataclass
import datetime


@dataclass
class TicketRequest:
	vehicle: str
	origin_city: str
	destination_city: str
	passengers: dict
	departue_date: datetime.datetime
	price_range: tuple[int]
	time_range: tuple[datetime.time]
	return_date: datetime.datetime | None = None
	one_way: bool = True
	class_type: str | None = None


@dataclass
class Ticket:
	departue_date: datetime.datetime
	departue_time: datetime.time
	avaiable_seat_count: int
	price: int
	description: str
	visit_url: str
	class_type: str
	company_name: str
	origin_location: str
	destination_location: str

	def to_dict(self) -> dict:
		return {
			"departue_date": self.departue_date,
			"departue_time": self.departue_time,
			"avaiable_seat_count": self.avaiable_seat_count,
			"price": self.price,
			"description": self.description,
			"visit_url": self.visit_url,
			"class_type": self.class_type,
			"company_name": self.company_name,
			"origin_location": self.origin_location,
			"destination_location": self.destination_location,
		}
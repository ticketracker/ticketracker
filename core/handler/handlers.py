from abc import ABC, abstractmethod
from typing import Optional

import requests
import jdatetime
import datetime

from core.ticket import Ticket, TicketRequest
from .cities import SAFAR724_CITIES


def get_city(name: str, city_list: list[dict]) -> Optional[dict]:
	# TODO: BIG(O) this function is not optimized. optimized later
	for city in city_list:
		if city['city'] == name:
			return city		
	return None


class Handler(ABC):

	@abstractmethod
	def search(self, input: TicketRequest) -> list[Ticket]: ...

	@abstractmethod
	def is_valid_ticket(input: TicketRequest, service: dict) -> bool: ...

	@abstractmethod
	def to_ticket(service: dict, ticket_request: TicketRequest) -> Ticket: ...

	def __str__(self):
		return '"Handler(%s)"' % self.__class__.__name__.rstrip("Handler")

	def __repr__(self):
		return '"Handler(%s)"' % self.__class__.__name__.rstrip("Handler")


class Safar724Handler(Handler):
	def search(self, ticket_request: TicketRequest) -> list[Ticket] | bool:
		"""Search trough the provider for specific input filters"""

		origin_city = get_city(ticket_request.origin_city, SAFAR724_CITIES)
		if not origin_city:
			print("city not found: %s" % ticket_request.origin_city)
			return False

		destination_city = get_city(ticket_request.destination_city, SAFAR724_CITIES)
		if not destination_city:
			print("city not found: %s" % ticket_request.destination_city)
			return False

		response = requests.get(
			url="https://safar724.com/bus/getservices",
			params={
				"origin": origin_city["code"],
				"destination": destination_city["code"],
				"date": jdatetime.datetime.fromtimestamp(ticket_request.departue_date.timestamp()).strftime("%Y-%m-%d")
			}
		)
		if response.status_code != 200:
			print("something went wrong")
			return False

		data = response.json()
		services = data['Items']
		if not services:
			return False

		filtered_ticket = [
			self.to_ticket(
				service,
				ticket_request,
				persion_origin_city=data['OriginPersianName'],
				persian_dest_city=data['DestinationPersianName'],
				eng_org_city=data['OriginEnglishName'],
				eng_dest_city=data['DestinationEnglishName'],
			)
			for service in services
			if self.is_valid_ticket(ticket_request, service)
		]
		return filtered_ticket

	@staticmethod
	def is_valid_ticket(ticket_request: TicketRequest, service: dict) -> bool:
		return (
			(ticket_request.price_range[0] <= service['Price'] <= ticket_request.price_range[1]) and
			(service['AvailableSeatCount'] >= sum(ticket_request.passengers.values())) and
			(ticket_request.time_range[0] <= datetime.datetime.strptime(service['DepartureTime'], '%H:%M').time() <= ticket_request.time_range[1])
		)

	@staticmethod
	def to_ticket(service: dict, ticket_request: TicketRequest, **meta) -> Ticket:
		"""Convert service dict to ticket object"""
		visit_url = "https://safar724.com/bus/%(org)s-%(dest)s?date=%(date)s/#/service:%(id)s-%(tcode)s" % {
			'org': meta['eng_org_city'],
			'dest': meta['eng_dest_city'],
			'date': service['DepartureDate'].replace('/', '-'),
			'id': service['ID'],
			'tcode': service['DestinationTerminalCode']
		}
		return Ticket(
			departue_date=service['DepartureDate'],
			departue_time=service['DepartureTime'],
			avaiable_seat_count=service['AvailableSeatCount'],
			price=service['Price'],
			description=service['Description'],
			visit_url=visit_url,
			class_type=service['BusType'],
			company_name=service['CompanyPersianName'],
			origin_location='%s پایانه %s' % (meta['persion_origin_city'], service['OriginTerminalPersianName']),
			destination_location='%s پایانه %s' % (meta['persian_dest_city'], service['DestinationTerminalPersianName']),
		)


class AlibabaHandler(Handler):
	def search(self, ticket_request: TicketRequest) -> list[Ticket]:
		"""Search trough the provider for specific input filters"""
		pass

	def is_valid_ticket(input: TicketRequest, service: dict) -> bool:
		"""Check the service is valid for given request or not"""

	def to_ticket(service: dict, ticket_request: TicketRequest, **meta) -> Ticket:
		"""Convert service dict to ticker object"""


class MrbilitHandler(Handler):
	def search(self, ticket_request: TicketRequest) -> list[Ticket]:
		"""Search trough the provider for specific input filters"""
		pass

	def is_valid_ticket(input: TicketRequest, service: dict) -> bool:
		"""Check the service is valid for given request or not"""

	def to_ticket(service: dict, ticket_request: TicketRequest, **meta) -> Ticket:
		"""Convert service dict to ticker object"""


class SafarmarketHandler(Handler):
	def search(self, ticket_request: TicketRequest) -> list[Ticket]:
		"""Search trough the provider for specific input filters"""
		pass

	def is_valid_ticket(input: TicketRequest, service: dict) -> bool:
		"""Check the service is valid for given request or not"""

	def to_ticket(service: dict, ticket_request: TicketRequest, **meta) -> Ticket:
		"""Convert service dict to ticker object"""


class Ghasedak24Handler(Handler):
	def search(self, ticket_request: TicketRequest) -> list[Ticket]:
		"""Search trough the provider for specific input filters"""
		pass

	def is_valid_ticket(input: TicketRequest, service: dict) -> bool:
		"""Check the service is valid for given request or not"""

	def to_ticket(service: dict, ticket_request: TicketRequest, **meta) -> Ticket:
		"""Convert service dict to ticker object"""


class EligashtHandler(Handler):
	def search(self, ticket_request: TicketRequest) -> list[Ticket]:
		"""Search trough the provider for specific input filters"""
		pass

	def is_valid_ticket(input: TicketRequest, service: dict) -> bool:
		"""Check the service is valid for given request or not"""

	def to_ticket(service: dict, ticket_request: TicketRequest, **meta) -> Ticket:
		"""Convert service dict to ticker object"""


class RajaHandler(Handler):
	def search(self, ticket_request: TicketRequest) -> list[Ticket]:
		"""Search trough the provider for specific input filters"""
		pass

	def is_valid_ticket(input: TicketRequest, service: dict) -> bool:
		"""Check the service is valid for given request or not"""

	def to_ticket(service: dict, ticket_request: TicketRequest, **meta) -> Ticket:
		"""Convert service dict to ticker object"""


class FlytodayHandler(Handler):
	def search(self, ticket_request: TicketRequest) -> list[Ticket]:
		"""Search trough the provider for specific input filters"""
		pass

	def is_valid_ticket(input: TicketRequest, service: dict) -> bool:
		"""Check the service is valid for given request or not"""

	def to_ticket(service: dict, ticket_request: TicketRequest, **meta) -> Ticket:
		"""Convert service dict to ticker object"""

from abc import ABC, abstractmethod

from core.ticket import Ticket, TicketRequest


class Handler(ABC):
	@abstractmethod
	def search(self, input: TicketRequest) -> list[Ticket]:
		"""Packing tickets for given input"""
		pass

	def __str__(self):
		return '"Handler(%s)"' % self.__class__.__name__.rstrip("Handler")

	def __repr__(self):
		return '"Handler(%s)"' % self.__class__.__name__.rstrip("Handler")



class Safar724Handler(Handler):
	def search(self, ticket_request: TicketRequest) -> list[Ticket]:
		"""Search trough the provider for specific input filters"""
		pass


class AlibabaHandler(Handler):
	def search(self, ticket_request: TicketRequest) -> list[Ticket]:
		"""Search trough the provider for specific input filters"""
		pass


class MrbilitHandler(Handler):
	def search(self, ticket_request: TicketRequest) -> list[Ticket]:
		"""Search trough the provider for specific input filters"""
		pass


class SafarmarketHandler(Handler):
	def search(self, ticket_request: TicketRequest) -> list[Ticket]:
		"""Search trough the provider for specific input filters"""
		pass


class Ghasedak24Handler(Handler):
	def search(self, ticket_request: TicketRequest) -> list[Ticket]:
		"""Search trough the provider for specific input filters"""
		pass


class EligashtHandler(Handler):
	def search(self, ticket_request: TicketRequest) -> list[Ticket]:
		"""Search trough the provider for specific input filters"""
		pass


class RajaHandler(Handler):
	def search(self, ticket_request: TicketRequest) -> list[Ticket]:
		"""Search trough the provider for specific input filters"""
		pass


class FlytodayHandler(Handler):
	def search(self, ticket_request: TicketRequest) -> list[Ticket]:
		"""Search trough the provider for specific input filters"""
		pass

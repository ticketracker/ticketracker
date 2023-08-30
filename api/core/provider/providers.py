from enum import Enum
from dataclasses import dataclass

from core.handler import (
	Handler,
	Safar724Handler,
	AlibabaHandler,
	MrbilitHandler,
	SafarmarketHandler,
	Ghasedak24Handler,
	EligashtHandler,
	RajaHandler,
	FlytodayHandler,
)


class Vehicle(Enum):
	BUS = "BUS"
	TRAIN = "TRAIN"
	AIRPLANE = "AIRPLANE"
	SHIP = "SHIP"
	ALL = "ALL"


@dataclass
class Provider:
	name: str
	vehicles: list[Vehicle] | Vehicle
	handler: Handler

	def __post_init__(self):
		self.vehicles = self.vehicles if isinstance(self.vehicles, list) else [self.vehicles]

	def support_vehicle(self, vehicle: str):
		return vehicle in [v.name for v in self.vehicles]


providers_list = {
	"safar724": Provider("safar724", Vehicle.BUS, Safar724Handler()),
	"alibaba": Provider("alibaba", [Vehicle.BUS, Vehicle.AIRPLANE, Vehicle.TRAIN], AlibabaHandler()),
	"mrbilit": Provider("mrbilit", Vehicle.ALL, MrbilitHandler()),
	"safarmarket": Provider("safarmarket", [Vehicle.AIRPLANE, Vehicle.TRAIN], SafarmarketHandler()),
	"ghasedak24": Provider("ghasedak24", [Vehicle.BUS, Vehicle.AIRPLANE, Vehicle.TRAIN], Ghasedak24Handler()),
	"eligasht": Provider("eligasht", [Vehicle.AIRPLANE, Vehicle.TRAIN], EligashtHandler()),
	"raja": Provider("raja", Vehicle.TRAIN, RajaHandler()),
	"flytoday": Provider("flytoday", Vehicle.AIRPLANE, FlytodayHandler()),
}

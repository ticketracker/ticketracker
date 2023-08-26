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


providers_list = [
	Provider("safar724", Vehicle.BUS, Safar724Handler()),
	Provider("alibaba", [Vehicle.BUS, Vehicle.AIRPLANE, Vehicle.TRAIN], AlibabaHandler()),
	Provider("mrbilit", Vehicle.ALL, MrbilitHandler()),
	Provider("safarmarket", [Vehicle.AIRPLANE, Vehicle.TRAIN], SafarmarketHandler()),
	Provider("ghasedak24", [Vehicle.BUS, Vehicle.AIRPLANE, Vehicle.TRAIN], Ghasedak24Handler()),
	Provider("eligasht", [Vehicle.AIRPLANE, Vehicle.TRAIN], EligashtHandler()),
	Provider("raja", Vehicle.TRAIN, RajaHandler()),
	Provider("flytoday", Vehicle.AIRPLANE, FlytodayHandler()),
]

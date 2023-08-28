# Core documentation


## a brief introduction

the core is responsible to manage trackers, recieve user's intended ticket, send to user and so on, as it called the **core**<br/>
the main codes for recieving tickets from providers are there (in **core** directory)

there are some modules that you may need to know to understand how core works:
- [*provider*](#providers)
- [*handler*](#handlers)
- [*ticket*](#tickets)
- [*tracker*](#tracker)


# Providers

**description:** *providers* are those applications/websites that we're using for packing tickets/services

[\[code\]](https://github.com/amirhosseinzibaei/ticketracker/blob/main/core/provider/providers.py)
```python

@dataclass
class Provider:
	name: str
	vehicles: list[Vehicle] | Vehicle
	handler: Handle

```

describe methods:
- *name*: it's the name of provider to recognize what provider is tracking
- *vehicles**: it's the providers's ticket avaiable vehicles for example ["Bus", "Airplane", "Train", "Ship"] (note: the *Vehicle* class is enum)
- *handler*: each provider has it's own handler that comes from *Handler* abstract class, this class is responsible to search over the provider's website to recieve ticket


# Handlers

**description:** each provider has it's own handler object and handlers are the most important things in the core. because they are responsible to collect tickets from provider's websites (they are our crawlers)

[\[code\]](https://github.com/amirhosseinzibaei/ticketracker/blob/main/core/handler/handlers.py)
```python

class Handler(ABC):

	@abstractmethod
	async def search(self, input: TicketRequest) -> list[Ticket]: ...

	@abstractmethod
	def is_valid_ticket(input: TicketRequest, service: dict) -> bool: ...

	@abstractmethod
	def to_ticket(service: dict, ticket_request: TicketRequest) -> Ticket: ...

```

> Note: this is an abstract class, so if there is a provider called `ABC`
> we need to create a class that inhreit from this class. like bellow
>>```python
>>class ABCHandler(Handler):
>>
>>	async def search(self, input: TicketRequest) -> list[Ticket]:
>>		# codes for this handler's search comes here
>>
>>	def is_valid_ticket(input: TicketRequest, service: dict) -> bool: ...
>>		# codes for this handler's is_valid_ticket comes here
>>
>>	def to_ticket(service: dict, ticket_request: TicketRequest) -> Ticket: ...
>>		# codes for this handler's to_ticket comes here
>>```


describe methods:
- *search*: this method is responsible to collect tickets of given `input: TicketRequests` and returns a list of requested tickets, (note: it returns False if no ticket collected)
- *is_valid_ticket*: this method calls in *search* method, just pass the ticket information and returns *True* if that ticket is our intended ticket or returns *False*
- *to_ticket*: and also this method calls in *search* method, and just return a `Ticket` object that fitted of given ticket information as dict


# Tickets:


**descriptions:** in ticket module there are two class, one `TicketRequest` and `Ticket`
the `TicketRequest` is the user's intended tickets. for exmpale: imagine user wants to recieve tickets of this information:
- ticket is for `Train` vehicle
- departue date is `2024 November 23`
- price ranges is `1,000,000 Rial -> 2,000,000 Rial`
- origin city and destination city is : 'Tehran' -> 'Shiraz'
- is this one way ticket or two way?
- and so on ...

and the `Ticket` class is recieved tickets in our form. if handlers tracks ticket, they use this class to return their ticket (just to be more cleaner and easier)


[\[code\]](https://github.com/amirhosseinzibaei/ticketracker/blob/main/core/ticket/tickets.py)

```python
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

	def to_dict(self) -> dict: ...

```

this is our code for class. (just look at the clsses's attribute to feel comport with them)



# Tracker

**description:** this class is most important things in the code, becouse this class is responsible to search over provider's handler
and if tracks something(tickets) with given `TicketReqest`, send the ticket information to the user


[\[code\]](https://github.com/amirhosseinzibaei/ticketracker/blob/main/core/tracker/tracker.py)

```python
@dataclass
class Tracker:
	id : Optional[uuid.uuid4] = field(init=False)
	ticket_request: TicketRequest
	providers: dict[Provider] | Provider = field(repr=False)
	active_duration: datetime.timedelta
	report_to: str

	def __post_init__(self):
		self.id = uuid.uuid4()

	async def start_tracking(self) -> None:
		"""Main code for start tracking tickets"""

	async def track(self, provider: Provider) -> None:
		"""Track for each provider"""
		
```

describe class:
- *id*: it's a uuid version 4, that is the id for tracker
- *ticker_request*: the user intended ticket request
- *providers*: which providers to serach over them, maybe a user just one to track from specific providers not all of them
- *active_duration*: well each tracker has it's own active duration time, and tracker is just active for that time, for exmaple user wants Tracker to tracks his/her intended ticket for *1 day*, and the tracker goes tracking just for 1day not less not more
- *reprot_to*: if tracker found something, it will reports to that given 'Email Address' / 'Phone number' or 'Telegram ID'

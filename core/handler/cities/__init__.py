import json
from pathlib import Path


PWD = Path(__file__).parent


with open(PWD / 'safar724.json') as file:
	SAFAR724_CITIES = json.load(file)

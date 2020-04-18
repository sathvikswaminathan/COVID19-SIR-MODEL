import requests 
import json

URL = "https://www.curecovid19.in/readings/readings/countrywise"

r = requests.get(URL)

response = json.loads(r.text)

POPULATION = 
{
"China": 1401855920,
"India": 1360053900,
"US": 329488021,
"Spain": 47100396,
"Italy": 60243406
}

def get_cases(country):
	# key -> country, value -> cases
	for key, value in response["counts"].items():
		if key == country:
			# list of infected cases
			return value 
		else:
			# error
			print("Country not included/ doesn't exist")
			return ("Error")

def get_population(country):
	# key -> country, value -> population
	for key, value in POPULATION.items():
		if key == country:
			return value 
		else:
			# error
			print("Country not included/ doesn't exist")
			return("Error")
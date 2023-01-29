travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
def add_new_country(country2, visits2, cities2):
  new_country = {}
  new_country["country"] = country2
  new_country["visits"] = visits2
  new_country["cities"] = cities2
  travel_log.append(new_country) # tylko przy dodawaniu do list []

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

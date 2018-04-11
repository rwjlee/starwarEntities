from SWDS import SWDS
from starwars_entities import Person, Planet, Species, Starship, Vehicle

swds = SWDS()

entity_tuple = [(Person, "https://swapi.co/api/people/?page=1"), 
    (Species, "https://swapi.co/api/species/?page=1"),
    (Starship, "https://swapi.co/api/starships/?page=1"),
    (Vehicle, "https://swapi.co/api/vehicles/?page=1"),
    (Planet, "https://swapi.co/api/planets/?page=1")]

for value in entity_tuple:
    obj, next_url = value
    swds.populate(obj, next_url)
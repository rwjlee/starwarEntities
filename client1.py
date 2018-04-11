import json, requests
from pprint import pprint

from starwars_entities import Person, Planet, Species, Starship, Vehicle
from base import DbManager

db = DbManager()

API_BASE="https://swapi.co/api/"

def get_json(url):
    resp = requests.get(url)
    if resp.status_code!=200:
        return None
    return json.loads(resp.text)

def save_entity(url, obj):
    json_data= get_json(url)
    
    entity = obj()
    entity.parse_json(json_data)

    db.save(entity)

def populate(obj, next_url):
    while next_url:
        group_data=get_json(next_url)
        results = group_data['results']

        for row in results:
            url = row['url']
            results = db.open().query(obj).filter(obj.url == url).all()

            if len(results)==0:
                save_entity(url, obj)
                # print(url)

        next_url=group_data['next']
        # next_url = None


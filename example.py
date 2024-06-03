from gj_api import GoJauntlyApi
import json

client = GoJauntlyApi(
    key_id="[KEY ID]",
    key_file="[PEM FILE]",
    issuer_id="[ISSUER ID]"
)

def example_curated_walk_search():
    response = client.curated_walk_search(data={
        # "lat": 52.414337,
        # "lon": -4.081806,
        "postcode" : "W1J 9BR",
        "radius": 2,
        # "username": "gojauntly",
        # "sort": "latest",
        "page": 0,
        "amount": 25,
    })
    print(json.dumps(response))
    
def example_curated_walk_retrieve():
    response = client.curated_walk_retrieve(id="1260831589854876137", data={
        "includeSteps": True
    })
    print(json.dumps(response))

def example_dynamic_routes_route():
    response = client.dynamic_routes_route(data={
        "points" : [
            [
            51.440300000000001,
            -2.5899399999999999
            ],
            [
            51.457189999999997,
            -2.5912000000000002
            ]
        ],
        "points_encoded" : True,
        "details" : [
            "potentially_unsuitable",
            "potentially_private",
            "road_environment"
        ],
        "instructions" : True,
        "profile" : "greenest",
        "max_paths" : 2
    })
    print(json.dumps(response))
    
def example_dynamic_routes_circular():
    response = client.dynamic_routes_circular(data={
        "start_point": [51.5073386, -0.1412785], # OR postcode
        # "postcode" : "W1J 9BR",
        "ditance": 2000,
        "points_encoded" : True,
        "details" : [
            "potentially_unsuitable",
            "potentially_private",
            "road_environment"
        ],
        "profile" : "greenest",
        "max_paths" : 2
    })
    print(json.dumps(response))
    
def example_dynamic_routes_circular_collection():
    response = client.dynamic_routes_circular_collection(data={
        "categorise": True, # If to return routes in categories like parks and woodland, where available
        "start_point": [51.5073386, -0.1412785], # OR postcode
        # "postcode" : "W1J 9BR",
        "distances": [1000, 2000, 4000],
        "points_encoded" : True,
        "details" : [
            "potentially_unsuitable",
            "potentially_private",
            "road_environment"
        ],
        "profile" : "greenest"
    })
    print(json.dumps(response))

example_curated_walk_retrieve()
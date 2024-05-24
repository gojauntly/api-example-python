from gj_api import GoJauntlyApi

client = GoJauntlyApi(
    key_id="[KEY ID]",
    key_file="[PEM FILE]",
    issuer_id="[ISSUER ID]"
)

def example_curated_walk_search():
    response = client.curated_walk_search(data={
        "_lon": -4.081806,
        "version": 11,
        "_radius": 2,
        "amount": 25,
        "_lat": 52.414337,
        "premiumLevel": 1,
        "visibility": -50,
        "attributes": [],
        "username": "gojauntly",
        "types": [
            "normal",
            "track"
        ],
        "page": 0,
        "premiumLevelOperator": "<=",
        "sort": "rankHighest"
    })
    print(response)
    
def example_curated_walk_retrieve():
    response = client.curated_walk_retrieve(id="14312567863811772911", data={"shallow": False})
    print(response)
    

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
            "potentially_unsuitable"
        ],
        "instructions" : True,
        "profile" : "greenest",
        "max_paths" : 2
    })
    print(response)

example_dynamic_routes_route()
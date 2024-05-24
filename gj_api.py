from datetime import datetime, timedelta
from enum import Enum
import requests
import jwt
import time
import json

ALGORITHM = 'ES256'
BASE_API = "https://connect.gojauntly.com"

class HttpMethod(Enum):
    GET = 1
    POST = 2

class GoJauntlyApiError(Exception):
    pass

class GoJauntlyApi:

    def __init__(self, key_id: str, key_file: str, issuer_id: str):
        self._token = None
        self.token_gen_date = None
        self.exp = None
        self.key_id = key_id
        self.key_file = key_file
        self.issuer_id = issuer_id
        self._debug = False
        _ = self.token  # generate first token

    def _generate_token(self):
        try:
            key = open(self.key_file, 'r').read()
        except IOError as _:
            key = self.key_file
        self.token_gen_date = datetime.now()
        exp = int(time.mktime((self.token_gen_date + timedelta(minutes=20)).timetuple()))
        payload = {
            'iss': self.issuer_id, 
            'exp': exp, 
            'aud': 'gojauntly-api-v1'
        }
        headers = {
            'kid': self.key_id, 
            'typ': 'JWT'
        }
        return jwt.encode(payload=payload, key=key, headers=headers, algorithm=ALGORITHM)

    def _api_call(self, url: str, method: HttpMethod, data: dict = None):
        url = f"{BASE_API}{url}"
        headers = {
            "Authorization": "Bearer %s" % self.token
        }
        if self._debug:
            print(url)
        r = {}

        if method == HttpMethod.GET:
            r = requests.get(url, headers=headers)
        elif method == HttpMethod.POST:
            headers["Content-Type"] = "application/json"
            r = requests.post(url=url, headers=headers, data=json.dumps(data))

        content_type = r.headers['content-type']

        if content_type in [ "application/json", "application/vnd.api+json" ]:
            payload = r.json()
            if 'errors' in payload:
                raise GoJauntlyApiError(payload.get('errors', [])[0].get('detail', 'Unknown error'))
            return payload
        else:
            if not 200 <= r.status_code <= 299:
                raise GoJauntlyApiError("HTTP error [%d][%s]" % (r.status_code, r.content))
            return r

    @property
    def token(self):
        # generate a new token every 15 minutes
        if (self._token is None) or (self.token_gen_date + timedelta(minutes=15) < datetime.now()):
            self._token = self._generate_token()

        return self._token
    
    def curated_walk_search(self, data: dict):
        payload = self._api_call(url="/curated-walks/search", method=HttpMethod.POST, data=data)
        return payload
    
    def curated_walk_retrieve(self, id: str, data: dict):
        payload = self._api_call(url=f"/curated-walks/{id}", method=HttpMethod.POST, data=data)
        return payload
    
    def dynamic_routes_route(self, data: dict):
        payload = self._api_call(url="/routing/route", method=HttpMethod.POST, data=data)
        return payload
    
    def dynamic_routes_circular(self, data: dict):
        payload = self._api_call(url="/routing/circular", method=HttpMethod.POST, data=data)
        return payload
    
    def dynamic_routes_circular_collection(self, data: dict):
        payload = self._api_call(url="/routing/circular/collection", method=HttpMethod.POST, data=data)
        return payload

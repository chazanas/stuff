#! /usr/bin/env python
from __future__ import print_function
import base64
import json
import urllib
import urllib2

TEST = 'a58f4577b8768f5b500a0e7715d8f526'
ESCALA_ANDROID = '2b7a4738c81462f1a47184db55b0e7a4'
ESCALA_IOS = '5a3e81bd96cb62d9862a3b22d559e363'
LACOS_WEB = 'b669d6a98bf5ef31b2578d4cee2d868d'


class Mixpanel(object):

    ENDPOINT_form = 'https://mixpanel.com/api'
    ENDPOINT_raw = 'https://data.mixpanel.com/api'
    VERSION = '2.0'

    def __init__(self, api_secret):
        self.api_secret = api_secret

    def request(self, methods, params={}, http_method='GET', format='json', raw=False):
        """
            methods - List of methods to be joined, e.g. ['events', 'properties', 'values']
                      will give us http://mixpanel.com/api/2.0/events/properties/values/
            params - Extra parameters associated with method
        """
        params['format'] = format

        if not raw:
            endpoint = self.ENDPOINT_form
        else:
            endpoint = self.ENDPOINT_raw
        
        request_url = '/'.join([endpoint, str(self.VERSION)] + methods)
        print (request_url)
        if http_method == 'GET':
            data = None
            request_url = request_url + '/?' + self.unicode_urlencode(params)
        else:
            data = self.unicode_urlencode(params)

        headers = {'Authorization': 'Basic {encoded_secret}'.format(encoded_secret=base64.b64encode(self.api_secret))}
        request = urllib2.Request(request_url, data, headers)
        response = urllib2.urlopen(request, timeout=120)
        if not raw:
            return json.loads(response.read())
        return response

    def unicode_urlencode(self, params):
        """
            Convert lists to JSON encoded strings, and correctly handle any
            unicode URL parameters.
        """
        if isinstance(params, dict):
            params = params.items()
        for i, param in enumerate(params):
            if isinstance(param[1], list):
                params[i] = (param[0], json.dumps(param[1]),)

        return urllib.urlencode(
            [(k, isinstance(v, unicode) and v.encode('utf-8') or v) for k, v in params]
        )

def list_mixpanel_events(events, api_secret=ESCALA_ANDROID, interval=60, unit='day', events_type='general'):
    """(int, str, list) -> dict
    return a dictionary with the data of the events in some period"""

    # === Request config ===
    api = Mixpanel(api_secret=api_secret)
    data = api.request(['events'], {
        'event': events,
        'unit': unit,
        'interval': interval,
        'type': events_type
    })

    return data
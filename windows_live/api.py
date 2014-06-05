'''
Created on 05 Jun 2014

@author: michael
'''
import requests

from windows_live import exceptions


def get_access_token_url(client_id, redirect_uri, scope='wl.signin,wl.emails'):
    url = "https://login.live.com/oauth20_authorize.srf"
    payload = {
        'client_id': client_id,
        'scope': scope,
        'response_type': 'code',
        'redirect_uri': redirect_uri
    }
    r = requests.get(url, params=payload)
    return r.url


def get_access_token_from_code(code, redirect_uri, client_id,
                               client_secret, scope='wl.signin,wl.emails'):
    url = "https://login.live.com/oauth20_token.srf"
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri
    }
    r = requests.get(url, params=payload)
    response_json = r.json()
    if 'error' in response_json:
        raise exceptions.AuthorizationException(
            '%s: %s' % (
                response_json['error'],
                response_json['error_description']
            )
        )
    return response_json


class Client(object):
    API_URL = 'https://apis.live.net/v5.0/'

    def __init__(self, access_token):
        self.params = {
            'access_token': access_token
        }

    def get(self, domain, params=None):
        if params is not None:
            assert isinstance(params, dict)
            self.params.update(params)
        r = requests.get(
            '%s%s/' % (self.API_URL, domain),
            params=self.params
        )
        return r.json()

    def post(self, domain, data, params=None, content_type='application/json'):
        if params is not None:
            assert isinstance(params, dict)
            self.params.update(params)
        headers = {
            'content-type': content_type
        }
        r = requests.post(
            '%s%s/' % (self.API_URL, domain),
            headers=headers,
            data=data,
            params=self.params
        )
        return r.json()

    def put(self, domain, data, params=None, content_type='application/json'):
        if params is not None:
            assert isinstance(params, dict)
            self.params.update(params)
        headers = {
            'content-type': content_type
        }
        r = requests.put(
            '%s%s/' % (self.API_URL, domain),
            headers=headers,
            data=data,
            params=self.params
        )
        return r.json()

    def delete(self, domain, params=None):
        if params is not None:
            assert isinstance(params, dict)
            self.params.update(params)
        r = requests.delete(
            '%s%s/' % (self.API_URL, domain),
            params=self.params
        )
        return r.json()

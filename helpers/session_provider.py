import requests

from helpers.endpoints import RestfullBookerEndpointBuilder


class GetToken:
    def __init__(self):
        self.user = "admin"
        self.password = "password123"

    def default_session(self):
        """Returns session with authentication token"""
        session = requests.Session()
        response = session.post(RestfullBookerEndpointBuilder.auth_url, json=self.body).json()
        session.headers.update({'Cookie': 'token='+response['token']})
        return session

    @property
    def body(self):
        return {
            "username": self.user,
            "password": self.password
        }




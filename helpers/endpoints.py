from config import config


class RestfullBookerEndpointBuilder:
    auth_url = f'{config.BASE_URL}/auth'
    booking = f'{config.BASE_URL}/booking'

    @classmethod
    def booking_by_id(cls, id):
        return f'{cls.booking}/{id}'

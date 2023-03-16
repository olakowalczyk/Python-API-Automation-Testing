import random

from utils.http_manager import HttpManager

class Bookings:

    BASE_URL = "https://restful-booker.herokuapp.com"
    PING = BASE_URL + "/ping"
    AUTH = BASE_URL + "/auth"
    GET_BOOKINGS = BASE_URL + "/booking/"
    GET_BOOKING = BASE_URL + "/booking/{0}"
    CREATE_BOOKING = BASE_URL + "/booking"
    DELETE_BOOKING = BASE_URL + "/booking/{0}"

    @classmethod
    def get_random_booking(cls):
        '''Chooses one booking from the list of currently existing ones'''
        return str(random.choice(cls.get_existing_bookings()))

    @staticmethod
    def get_existing_bookings():
        '''Provides the list of currently existing bookings'''
        url = f'{Bookings.BASE_URL}/booking'
        response = (HttpManager.get(url))
        return [booking['bookingid'] for booking in response.json()]

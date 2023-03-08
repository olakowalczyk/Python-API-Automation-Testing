import requests
import random


class Bookings:

    BASE_URL = "https://restful-booker.herokuapp.com"

    @classmethod
    def get_random_booking(cls):
        '''Chooses one booking from the list of currently existing ones'''
        return random.choice(cls.get_existing_bookings())

    @staticmethod
    def get_existing_bookings():
        '''Provides the list of currently existing bookings'''
        url = f'{Bookings.BASE_URL}/booking'
        response = (requests.get(url)).json()
        return [booking['bookingid'] for booking in response]

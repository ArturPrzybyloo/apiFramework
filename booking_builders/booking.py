from dataclasses import dataclass

from helpers.endpoints import RestfullBookerEndpointBuilder
from helpers.session_provider import GetToken
from helpers.status_codes import StatusCodes
from helpers.utlis import verify_response_status_code

session = GetToken().default_session()


@dataclass
class Booking:
    first_name: str
    last_name: str
    total_price: int
    deposit_paid: bool
    additional_needs: str
    checkin: str
    checkout: str
    id: int = None

    def create(self):
        response = session.post(RestfullBookerEndpointBuilder.booking, json=self.body)
        verify_response_status_code(response, StatusCodes.OK)
        self.id = response.json()['bookingid']
        return self

    def update(self, first_name: str, last_name: str, total_price: int, deposit_paid: bool, additional_needs: str,
               checkin: str, checkout: str):
        self.first_name = first_name
        self.last_name = last_name
        self.total_price = total_price
        self.deposit_paid = deposit_paid
        self.additional_needs = additional_needs
        self.checkin = checkin
        self.checkout = checkout
        response = session.put(RestfullBookerEndpointBuilder.booking_by_id(self.id), json=self.body)
        verify_response_status_code(response, StatusCodes.OK)
        return self

    def delete(self):
        response = session.delete(RestfullBookerEndpointBuilder.booking_by_id(self.id))
        verify_response_status_code(response, StatusCodes.CREATED)
        return self

    def get_all_ids(self):
        response = session.get(RestfullBookerEndpointBuilder.booking).json()
        ids = []
        for id in response:
            ids.append(id['bookingid'])
        return ids

    @property
    def body(self):
        return {
            "firstname": self.first_name,
            "lastname": self.last_name,
            "totalprice": self.total_price,
            "depositpaid": self.deposit_paid,
            "bookingdates": {
                "checkin": self.checkin,
                "checkout": self.checkout
            },
            "additionalneeds": self.additional_needs
        }


class BookingBuilder:
    def __init__(self, first_name: str, last_name: str, total_price: int, deposit_paid: bool, additional_needs: str,
                 checkin: str, checkout: str):
        self.first_name = first_name
        self.last_name = last_name
        self.total_price = total_price
        self.deposit_paid = deposit_paid
        self.additional_needs = additional_needs
        self.checkin = checkin
        self.checkout = checkout

    def add_booking(self) -> Booking:
        return Booking(first_name=self.first_name,
                       last_name=self.last_name,
                       total_price=self.total_price,
                       deposit_paid=self.deposit_paid,
                       additional_needs=self.additional_needs,
                       checkin=self.checkin,
                       checkout=self.checkout).create()


class BookingManager:

    def get_booking_by_id(self, booking_id, expected_status_code=StatusCodes.OK) -> Booking:
        response = session.get(RestfullBookerEndpointBuilder.booking_by_id(booking_id))
        verify_response_status_code(response, expected_status_code)
        if expected_status_code == StatusCodes.OK:
            booking = response.json()
            return Booking(first_name=booking['firstname'],
                           last_name=booking['lastname'],
                           total_price=booking['totalprice'],
                           deposit_paid=booking['depositpaid'],
                           additional_needs=booking['additionalneeds'],
                           checkin=booking['bookingdates']['checkin'],
                           checkout=booking['bookingdates']['checkout'],
                           id=booking_id)

from booking_builders.booking import BookingBuilder, BookingManager
from helpers import data_generator
from helpers.status_codes import StatusCodes
from helpers.utlis import assert_provided_data


class RestfullBookerTests:
    """Tests for CRUD methods for Resftull Booker open API"""
    manager = BookingManager()

    def test_booking(self):
        """E2E test for create, update and delete booking"""

        data = data_generator.generate_booking_data()
        new_booking = BookingBuilder(data['first_name'], data['last_name'], data['total_price'], data['deposit_paid'],
                                     data['additional_needs'], data['date'], data['date']).add_booking()
        added_booking = self.manager.get_booking_by_id(new_booking.id)
        assert_provided_data(new_booking, added_booking)
        all_ids = added_booking.get_all_ids()
        assert added_booking.id in all_ids, f'ID: {added_booking.id} not in all created bookings IDs'
        new_data = data_generator.generate_booking_data()
        added_booking.update(new_data['first_name'], new_data['last_name'], new_data['total_price'], new_data['deposit_paid'],
                       new_data['additional_needs'], new_data['date'], new_data['date'])
        booking_updated = self.manager.get_booking_by_id(new_booking.id)
        assert_provided_data(booking_updated.first_name, new_data['first_name'])
        assert_provided_data(booking_updated.last_name, new_data['last_name'])
        assert_provided_data(booking_updated.total_price, new_data['total_price'])
        booking_updated.delete()
        self.manager.get_booking_by_id(new_booking.id, StatusCodes.NOT_FOUND)
        all_ids = added_booking.get_all_ids()
        assert booking_updated.id not in all_ids, f'ID: {added_booking.id} found in all booking IDs'


if __name__ == '__main__':
    RestfullBookerTests().test_booking()

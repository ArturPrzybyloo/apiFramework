import random
from datetime import datetime

from faker import Faker


def generate_booking_data():
    """Returns map of random generated booking data"""
    fake = Faker('en_US')
    first_name = fake.first_name()
    last_name = fake.last_name()
    total_price = random.randint(20, 100)
    deposit_paid = fake.boolean()
    date = datetime.today().strftime('%Y-%m-%d')
    addotional_needs = ['Towels', 'Double bed', 'Car rental', 'Dinner', 'See view', 'All inclusive']
    return {"first_name": first_name,
            "last_name": last_name,
            "total_price": total_price,
            "deposit_paid": deposit_paid,
            "date": date,
            "additional_needs": addotional_needs[random.randint(0, 5)]}

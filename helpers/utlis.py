import json


class ResponseStatusCodeNotMatchedException(Exception):
    pass


def verify_response_status_code(response, expected_status_code):
    if response.status_code != expected_status_code:
        raise ResponseStatusCodeNotMatchedException(f'Expected status code: {expected_status_code} but was '
                                                    f'{response.status_code} \n with response: {response.text}')


def assert_provided_data(actual_value, expected_value):
    """:param - actual value - provide value from GET request
       :param - expected value - provide value that was send in POST/UPDATE request"""
    assert actual_value == expected_value, \
        f'Actual value: {actual_value} not matches expected value: {expected_value}'

import time

from basic_utility_functions.api_header_utitlity import set_api_header, \
    set_application_json_header
from basic_utility_functions.api_json_payload_utility import set_req_ver_json_payload, set_verification_json_payload, \
    set_address_chk_json_payload, set_initialize_json_payload, \
    set_first_payment_json_payload, set_contract_json_payload
from basic_utility_functions.api_methods_utitlity import set_api_post_method, set_api_get_method
from basic_utility_functions.common_utility import set_properties_config


def retailer_auth(retailer_name):
    response_api = set_api_post_method(
        set_properties_config()['API']['baseURI'] + set_properties_config()['API']['request_verification_code'],
        set_api_header(retailer_name),
        set_req_ver_json_payload('5674246714'))
    data = response_api.json()
    return data


def retailer_auth_verify(retailer_name):
    response_api = set_api_post_method(
        set_properties_config()['API']['baseURI'] + set_properties_config()['API']['customer_phone_lookup'],
        set_api_header(retailer_name),
        set_verification_json_payload('5674246714'))
    data = response_api.json()
    return data


def address_check_verify(retailer_name):
    response_api = set_api_post_method(
        set_properties_config()['API']['baseURI'] + set_properties_config()['API']['address_check'],
        set_api_header(retailer_name),
        set_address_chk_json_payload('5674246714'))
    data = response_api.json()
    return data


def cart_check_verify(retailer_name):
    response_api = set_api_post_method(
        set_properties_config()['API']['baseURI'] + set_properties_config()['API']['cart_check'],
        set_api_header(retailer_name),
        set_verification_json_payload('5674246714'))
    data = response_api.json()
    return data


def initialize_verify(ret_name):
    response_api = set_api_post_method(
        set_properties_config()['API']['baseURI'] + set_properties_config()['API']['initialize'],
        set_api_header(ret_name),
        set_initialize_json_payload('5674246714'))
    data = response_api.json()
    return data


def lease_verify_before_sync(ret_name):
    retailer_auth(ret_name)
    retailer_auth_verify(ret_name)
    address_check_verify(ret_name)
    cart_check_verify(ret_name)
    data = initialize_verify(ret_name)
    response_api = set_api_get_method(
        set_properties_config()['API']['baseURI'] + set_properties_config()['API']['lease'] + str(
            data['checkout_id']) +
        '/lease/',
        set_api_header(ret_name))
    data1 = response_api.json()
    response_api2 = set_api_get_method(
        set_properties_config()['API']['baseURI'] + set_properties_config()['API']['cart'] + data['uid'] + '/cart/',
        set_api_header(ret_name))
    data2 = response_api2.json()
    response_api3 = set_api_post_method(
        set_properties_config()['API']['baseURI'] + set_properties_config()['API']['contract'],
        set_application_json_header(),
        set_contract_json_payload(data['uid']))
    data3 = response_api3.json()
    response_api4 = set_api_post_method(
        set_properties_config()['API']['api_base_uri'] + '/v1/' + data['uid'] + set_properties_config()['API']
        ['first_payment'],
        set_api_header(ret_name),
        set_first_payment_json_payload())
    data4 = response_api4.json()
    time.sleep(10)
    return data

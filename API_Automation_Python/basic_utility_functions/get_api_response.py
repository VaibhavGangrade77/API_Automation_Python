import time

from basic_utility_functions.api_header_utitlity import *
from basic_utility_functions.api_json_payload_utility import *
from basic_utility_functions.api_methods_utitlity import *
from basic_utility_functions.before_sync_endpoint import lease_verify_before_sync
from basic_utility_functions.common_utility import *
from sync_endpoint.test_verify_sync_testCases import test_sync_with_valid_inputs


def get_sync_endpoint_response(ret_name):
    lease_dict = lease_verify_before_sync(ret_name)
    response_api = set_api_post_method(
        set_properties_config()['API']['baseURI'] + set_properties_config()['API']['sync'],
        set_api_header(ret_name),
        set_sync_json_payload(str(lease_dict['uid'])))
    data = response_api.json()
    time.sleep(3)
    return data
    # list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    # for i in range(1, 3):
    #     if list1[i] != 'Noretailer':


def get_vcc_sync_endpoint_response(ret_name):
    sync_dict = get_sync_endpoint_response(ret_name)
    vcc_sync_uid = set_vcc_sync_json_payload(sync_dict['uid'])
    response_api = set_api_post_method(
        set_properties_config()['API']['baseURI'] + set_properties_config()['API']['vcc_sync'],
        set_api_header(ret_name), vcc_sync_uid)
    data = response_api.json()
    time.sleep(3)
    return data



def get_dict_retailer_uid():
    uid_list = []
    ret_list = []
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        if list1[i] != 'Noretailer':
            ret_list.append(list1[i])
            uid_list.append(get_sync_endpoint_response('uid', list1[i]))
    ret_dict = get_retailer_dictionary(ret_list, uid_list)
    return ret_dict


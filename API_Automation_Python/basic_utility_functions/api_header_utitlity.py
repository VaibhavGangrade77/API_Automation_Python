import os
from basic_utility_functions.common_utility import *
from basic_utility_functions.file_operations_utility import *
from basic_utility_functions.jsondata import *


def set_retailer_list(col_num):
    read_file_info = read_file(filepath.retailer_info_filepath)
    retailer_arr = []
    for row in read_file_info:
        retailer_arr.append(row[col_num])
    return retailer_arr


def set_api_header(retailer_name):
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    list2 = set_retailer_list(int(set_properties_config()['COLUMNS']['col2']))
    ret_dict = get_retailer_dictionary(list1, list2)
    ret_json = {"Content-Type": 'application/json', "authorization": "Bearer " + ret_dict[retailer_name]}
    return ret_json


def set_api_header_text(retailer_name):
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    list2 = set_retailer_list(int(set_properties_config()['COLUMNS']['col2']))
    ret_dict = get_retailer_dictionary(list1, list2)
    ret_json = {"Content-Type": 'application/text', "authorization": 'Bearer ' + ret_dict[retailer_name]}
    return ret_json


def set_api_header_remove_Bearer(retailer_name):
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    list2 = set_retailer_list(int(set_properties_config()['COLUMNS']['col2']))
    ret_dict = get_retailer_dictionary(list1, list2)
    ret_json = {"Content-Type": 'application/json', "authorization": ret_dict[retailer_name]}
    return ret_json


def set_viewcard_authcode(param_val):
    set_json = {"authorization": 'Bearer ' + param_val}
    return set_json


def set_application_json_header():
    set_json = {"Content-Type": 'application/json'}
    return set_json


def set_viewcard_remove_bearer(param_val):
    set_json = {"authorization": param_val}
    return set_json


def create_file_name(dir_name, file_name, api_name, retailer_name):
    if not os.path.exists(dir_name):
        try:
            os.makedirs(dir_name)
        except Exception as e:
            print(e)
            raise
    with open(os.path.join(dir_name, retailer_name+"_"+api_name+"_"+file_name), 'w') as f:
        return f
    # os.chdir('../vab')
    # for file in glob.glob("*.json"):
    #     temp.append(file)
    # print(temp)


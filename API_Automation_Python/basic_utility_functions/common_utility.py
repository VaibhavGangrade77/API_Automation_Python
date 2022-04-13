import configparser


def set_properties_config():
    read_config = configparser.ConfigParser()
    read_config.read("../basic_utility_functions/properties.ini")
    return read_config


def add_newline_text(text_to_add):
    dashline = "+ " * 11
    return '\n' + ' ' + dashline + text_to_add + ' ' + dashline + '\n'


def get_retailer_dictionary(list1, list2):
    zip_it = zip(list1, list2)
    a_dict = dict(zip_it)
    return a_dict


def get_list_length(list_name):
    list_size = len(list_name)
    return list_size

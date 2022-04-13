import requests


def set_api_post_method(url, header_param, json_payload_param):
    session = requests.session()
    response_api = session.post(url, json=json_payload_param, headers=header_param, )
    return response_api


def set_api_get_method(url, header_param):
    session = requests.session()
    response_api = session.get(url, headers=header_param, )
    return response_api

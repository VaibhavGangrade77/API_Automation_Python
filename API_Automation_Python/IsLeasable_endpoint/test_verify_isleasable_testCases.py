import datetime
import json

import pytest
import requests

from basic_utility_functions.api_header_utitlity import set_api_header, set_retailer_list, set_api_header_text
from basic_utility_functions.api_json_payload_utility import set_isleasable_json_payload
from basic_utility_functions.api_methods_utitlity import set_api_post_method, set_api_get_method
from basic_utility_functions.common_utility import set_properties_config, add_newline_text
from basic_utility_functions.file_operations_utility import read_file, getWriteFilePath
from basic_utility_functions.jsondata import filepath


def before_test(colnum):
    read_file_info = read_file(filepath.leasable_file_path)
    testdata = []
    for row in read_file_info:
        testdata.append(row[colnum])
    return testdata


@pytest.mark.security
def test_with_valid_inputs():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        if list1[i] != 'Noretailer':
            outfile = getWriteFilePath("../isleasable_response_msg_file/" + list1[i] +
                                       "_valid_response_msg.json")
            response_api = set_api_post_method(
                set_properties_config()['API']['isLeaseURI'] + set_properties_config()['API']['isLeaseParam'],
                set_api_header(list1[i]),
                set_isleasable_json_payload(
                    before_test(int(set_properties_config()['COLUMNS']['col1']))))
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            data = response_api.json()
            outfile.write(list1[i] + " - Isleasable--Test Case :  Test with all the valid details")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("Response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            json.dump(before_test(int(set_properties_config()['COLUMNS']['col1'])), outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            json.dump(data, outfile, indent=1)
            outfile.write('\n')
            json.dump("Status Code: " + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 200, "Status code 200 expected in this case"
            outfile.close()
        else:
            break


@pytest.mark.security
def test_with_other_language_product_name():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        if list1[i] != 'Noretailer':
            outfile = getWriteFilePath(
                "../isleasable_response_msg_file/" + list1[i] + "_other_language_product_name_msg.json")
            response_api = set_api_post_method(
                set_properties_config()['API']['isLeaseURI'] + set_properties_config()['API']['isLeaseParam'],
                set_api_header(list1[i]),
                set_isleasable_json_payload(before_test(int(set_properties_config()['COLUMNS']['col2']))))
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            outfile.write(list1[i] + " -- Isleasable--Test Case : Verify with other language product name")
            data = response_api.json()
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            json.dump(before_test(int(set_properties_config()['COLUMNS']['col2'])), outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            json.dump(data, outfile, indent=1)
            outfile.write('\n')
            json.dump("Status Code: " + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 200, "Status code 200 expected in this case"
            outfile.close()


@pytest.mark.security
def test_with_no_product_name():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        if list1[i] != 'Noretailer':
            outfile = getWriteFilePath("../isleasable_response_msg_file/" + list1[i] + "_no_product_name_msg.json")
            response_api = set_api_post_method(
                set_properties_config()['API']['isLeaseURI'] + set_properties_config()['API']['isLeaseParam'],
                set_api_header(list1[i]),
                set_isleasable_json_payload(before_test(int(set_properties_config()['COLUMNS']['col3']))))
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            data = response_api.json()
            outfile.write(list1[i] + " -- Isleasable--Test Case : Verify with no product name in payload")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            json.dump(before_test(int(set_properties_config()['COLUMNS']['col3'])), outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            json.dump(data, outfile, indent=1)
            outfile.write('\n')
            json.dump("Status Code: " + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 200, "Status code 200 expected in this case"
            outfile.close()


@pytest.mark.security
def test_with_product_name_with_quote():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        if list1[i] != 'Noretailer':
            outfile = getWriteFilePath(
                "../isleasable_response_msg_file/" + list1[i] + "_product_name_with_quote_msg.json")
            response_api = set_api_post_method(
                set_properties_config()['API']['isLeaseURI'] + set_properties_config()['API']['isLeaseParam'],
                set_api_header(list1[i]),
                set_isleasable_json_payload(before_test(int(set_properties_config()['COLUMNS']['col4']))))
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            data = response_api.json()
            outfile.write(list1[i] + "-- isleasable--Test Case : Verify with product name which contains sing and "
                                     "double quote")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            json.dump(before_test(int(set_properties_config()['COLUMNS']['col4'])), outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            json.dump(data, outfile, indent=1)
            outfile.write('\n')
            json.dump("Status Code: " + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 200, "Status code 200 expected in this case"
            outfile.close()


@pytest.mark.security
def test_with_long_string_product_name():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        if list1[i] != 'Noretailer':
            outfile = getWriteFilePath(
                "../isleasable_response_msg_file/" + list1[i] + "_long_string_product_name_msg.json")
            response_api = set_api_post_method(
                set_properties_config()['API']['isLeaseURI'] + set_properties_config()['API']['isLeaseParam'],
                set_api_header(list1[i]),
                set_isleasable_json_payload(before_test(int(set_properties_config()['COLUMNS']['col5']))))
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            data = response_api.json()
            outfile.write(list1[i] + " -- Isleasable -- Test Case : Verify with long string product name")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            json.dump(before_test(int(set_properties_config()['COLUMNS']['col5'])), outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            json.dump(data, outfile, indent=1)
            outfile.write('\n')
            json.dump("Status Code: " + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 200, "Status code 200 expected in this case"
            outfile.close()


@pytest.mark.security
def test_with_empty_payload():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        if list1[i] != 'Noretailer':
            session = requests.session()
            outfile = getWriteFilePath("../isleasable_response_msg_file/" + list1[i] + "_empty_payload_msg.json")
            # response_api = set_api_post_method(setconfig()['API']['isLeaseURI'] + setconfig()['API']['isLeaseParam'],
            #                                    set_api_header("Noretailer"),
            #                                    set_isleasable_json_payload('null'))
            response_api = session.post(
                set_properties_config()['API']['isLeaseURI'] + set_properties_config()['API']['isLeaseParam'],
                json={},
                headers=set_api_header(list1[i]), )
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            data = response_api.json()
            outfile.write("Isaleasable -- Test Case : Verify with empty payload")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            json.dump("{}", outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            json.dump(data, outfile, indent=1)
            outfile.write('\n')
            json.dump("Status Code: " + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 200, "Status code 200 expected in this case"
            outfile.close()


@pytest.mark.security
def test_with_wrong_paramName_Payload():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        if list1[i] != 'Noretailer':
            session = requests.session()
            outfile = getWriteFilePath(
                "../isleasable_response_msg_file/" + list1[i] + "_wrong_paramName_Payload_msg.json")
            # response_api = set_api_post_method(setconfig()['API']['isLeaseURI'] + setconfig()['API']['isLeaseParam'],
            #                                    set_api_header("Noretailer"),
            #                                    set_isleasable_json_payload('null'))
            response_api = session.post(
                set_properties_config()['API']['isLeaseURI'] + set_properties_config()['API']['isLeaseParam'],
                json={"item_display_names": ["Mattress"]},
                headers=set_api_header("Noretailer"), )
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            data = response_api.json()
            outfile.write(
                list1[i] + " - Isleasable -- Test Case : Verify with wrong parameter name in the JSON payload")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            json.dump(before_test(int(set_properties_config()['COLUMNS']['col1'])), outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            json.dump(data, outfile, indent=1)
            outfile.write('\n')
            json.dump("Status Code: " + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 200, "Status code 200 expected in this case"
            outfile.close()


@pytest.mark.security
def test_with_with_HTTP_instead_of_HTTPS():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, 2):
        if list1[i] != 'Noretailer':
            session = requests.session()
            outfile = getWriteFilePath("../isleasable_response_msg_file/" + list1[i] + "_verify_http_protocol_msg.json")
            # response_api = set_api_post_method(setconfig()['API']['isLeaseURI'] + setconfig()['API']['isLeaseParam'],
            #                                    set_api_header("Noretailer"),
            #                                    set_isleasable_json_payload('null'))
            response_api = session.post(
                set_properties_config()['API']['http_isLeaseURI'] + set_properties_config()['API']['isLeaseParam'],
                json={"item_display_name": ["Mattress"]},
                headers=set_api_header(list1[i]), )
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            data = response_api.text
            outfile.write(list1[i] + " - Isleasable -- Test Case : Verify with HTTP protocol instead of HTTPS protocol")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            json.dump('{"item_display_names": "Mattress"}', outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            json.dump(data, outfile, indent=1)
            outfile.write('\n')
            json.dump("Status Code: " + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 400, "Status code 400 expected in this case"
            outfile.close()


@pytest.mark.security
def test_with_http_method_GET_instead_POST():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        if list1[i] != 'Noretailer':
            outfile = getWriteFilePath(
                "../isleasable_response_msg_file/" + list1[i] + "_verify_with_GET_method_msg.json")
            response_api = set_api_get_method(set_properties_config()['API']['isLeaseURI'] +
                                              set_properties_config()['API']['isLeaseParam'],
                                              set_api_header(list1[i]))

            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            data = response_api.text
            outfile.write(
                list1[i] +
                "- Isleasable -- Test Case : Verify with the GET method instead of the Post method")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            json.dump('{}', outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            json.dump(data, outfile, indent=1)
            outfile.write('\n')
            json.dump("Status Code: " + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 400, "Status code 400 expected in this case"
            outfile.close()


@pytest.mark.security
def test_with_application_type_text():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        if list1[i] != 'Noretailer':
            session = requests.session()
            outfile = getWriteFilePath("../isleasable_response_msg_file/"+list1[i]+
                                       "_verify_with_text_application_msg.json")
            response_api = set_api_post_method(
                set_properties_config()['API']['isLeaseURI'] + set_properties_config()['API']['isLeaseParam'],
                set_api_header_text(list1[i]),
                set_isleasable_json_payload(before_test(int(set_properties_config()['COLUMNS']['col1']))))
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            data = response_api.json()
            outfile.write(list1[i]+"- Isleasable -- Test Case : Verify with aaplication/text instead of "
                                   "application/json")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            json.dump(before_test(int(set_properties_config()['COLUMNS']['col1'])), outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            # outfile.write('\n')
            json.dump(data, outfile, indent=1)
            outfile.write('\n')
            json.dump("Status Code: " + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 200, "Status code 200 expected in this case"
            outfile.close()

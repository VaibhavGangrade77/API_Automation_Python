import datetime
import json
import time
import pytest

from basic_utility_functions.api_header_utitlity import *
from basic_utility_functions.api_json_payload_utility import *
from basic_utility_functions.api_methods_utitlity import *
from basic_utility_functions.before_sync_endpoint import lease_verify_before_sync, initialize_verify
from basic_utility_functions.common_utility import *
from basic_utility_functions.file_operations_utility import *


@pytest.mark.security
def test_sync_with_valid_inputs():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        if list1[i] != 'Noretailer':
            lease_dict = lease_verify_before_sync(list1[i])
            time.sleep(5)
            response_api = set_api_post_method(
                set_properties_config()['API']['baseURI'] + set_properties_config()['API']['sync'],
                set_api_header(list1[i]),
                set_sync_json_payload(str(lease_dict['uid'])))
            outfile = getWriteFilePath("../sync_response_msg_file/" + list1[i] + "_sync_valid_response_msg.json")
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            data = response_api.json()
            outfile.write(list1[i] + " - Sync Endpoint -- Test Case: Test with all the valid details")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("Response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            json.dump(set_sync_json_payload(str(lease_dict['uid'])), outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            json.dump(data, outfile)
            outfile.write('\n')
            json.dump("Status Code :" + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 200, "Status code 200 expected in this case"
            outfile.close()
        else:
            break


@pytest.mark.security
def test_sync_with_empty_UID_in_payload():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        if list1[i] != 'Noretailer':
            # lease_dict = lease_verify_before_sync(list1[i])
            # time.sleep(15)
            response_api = set_api_post_method(
                set_properties_config()['API']['baseURI'] + set_properties_config()['API']['sync'],
                set_api_header(list1[i]),
                set_sync_json_payload("NULL"))
            outfile = getWriteFilePath("../sync_response_msg_file/" + list1[i] +
                                       "_sync_with_empty_UID_in_json_payload_msg.json")
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            data = response_api.json()
            outfile.write(list1[i] + " - Sync Endpoint -- Test Case: Test with empty UID in the Payload")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("Response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            json.dump(set_sync_json_payload("NULL"), outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            json.dump(data, outfile)
            outfile.write('\n')
            json.dump("Status Code :" + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 404, "Status code 404 expected in this case"
            outfile.close()
        else:
            break


@pytest.mark.security
def test_sync_with_HTTP_instead_HTTPS():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        if list1[i] != 'Noretailer':
            lease_dict = lease_verify_before_sync(list1[i])
            time.sleep(5)
            response_api = set_api_post_method(
                set_properties_config()['API']['http_baseURI'] + set_properties_config()['API']['sync'],
                set_api_header(list1[i]),
                set_sync_json_payload(str(lease_dict['uid'])))
            outfile = getWriteFilePath(
                "../sync_response_msg_file/" + list1[i] + "_sync_verify_http_instead_https_msg.json")
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            # response_api.raise_for_status()
            data = response_api.text
            outfile.write(list1[i] + " - Sync Endpoint -- Test Case: Test with HTTP instead of the HTTPS protocol")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("Response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            json.dump(set_sync_json_payload(str(lease_dict['uid'])), outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            outfile.write('\n')
            json.dump(data, outfile, indent=1)
            outfile.write("\n")
            json.dump("Status Code :" + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 405, "Status code 405 expected in this case"
            outfile.close()
        else:
            break


@pytest.mark.security
def test_sync_with_invalid_bearer_token():
    outfile = getWriteFilePath(
        "../sync_response_msg_file/Noretailer_sync_verify_with_invalid_bearer_token_msg.json")
    response_api = set_api_post_method(
        set_properties_config()['API']['baseURI'] + set_properties_config()['API']['sync'],
        set_api_header('Noretailer'),
        set_sync_json_payload('978748873f4747f5800a7803d236878d'))
    respTime = str(round(response_api.elapsed.total_seconds(), 2))
    currDate = datetime.datetime.now()
    currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
    data = response_api.text
    outfile.write("Noretailer - Sync Endpoint -- Test Case: Test with the invalid or other retailer's key")
    outfile.write(add_newline_text("API URL and the request header as follows:"))
    json.dump(response_api.request.url, outfile, indent=1)
    outfile.write('\n')
    json.dump(dict(response_api.request.headers), outfile, indent=2)
    outfile.write(add_newline_text("Response time information:"))
    json.dump(currDate + " " + respTime, outfile, indent=2)
    outfile.write(add_newline_text("The request payload as follows:"))
    json.dump(set_sync_json_payload('978748873f4747f5800a7803d236878d' + 'abcde'), outfile, indent=1)
    outfile.write(add_newline_text("The response as follows:"))
    # outfile.write('\n')
    json.dump(data, outfile, indent=1)
    outfile.write("\n")
    json.dump("Status Code :" + str(response_api.status_code), outfile, indent=1)
    assert response_api.status_code == 401, "Status code 401 expected in this case"
    outfile.close()


@pytest.mark.security
def test_sync_with_invalid_UID():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        if list1[i] != 'Noretailer':
            lease_dict = lease_verify_before_sync(list1[i])
            time.sleep(5)
            response_api = set_api_post_method(
                set_properties_config()['API']['baseURI'] + set_properties_config()['API']['sync'],
                set_api_header(list1[i]),
                set_sync_json_payload(str(lease_dict['uid'])+'abcdef'))
            outfile = getWriteFilePath("../sync_response_msg_file/" + list1[i] + "_sync_with_invalid_UID_msg.json")
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            data = response_api.json()
            outfile.write(list1[i] + " - Sync Endpoint -- Test Case: Test with the invalid UID")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("Response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            json.dump(set_sync_json_payload(str(lease_dict['uid'])+'abcdef'), outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            json.dump(data, outfile)
            outfile.write('\n')
            json.dump("Status Code :" + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 404, "Status code 404 expected in this case"
            outfile.close()
        else:
            break


@pytest.mark.security
def test_sync_with_removing_bearer_word():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        if list1[i] != 'Noretailer':
            lease_dict = lease_verify_before_sync(list1[i])
            time.sleep(5)
            outfile = getWriteFilePath("../sync_response_msg_file/" + list1[i] + "_sync_removing_bearer_word_msg.json")
            response_api = set_api_post_method(
                set_properties_config()['API']['baseURI'] + set_properties_config()['API']['sync'],
                set_api_header_remove_Bearer(list1[i]),
                set_sync_json_payload(str(lease_dict['uid'])))
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            data = response_api.text
            outfile.write(
                list1[i] + " - Sync Endpoint -- Test Case: Test with removing the Bearer word from the payload")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("Response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            json.dump(set_sync_json_payload(str(lease_dict['uid'])), outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            # outfile.write('\n')
            json.dump("Response Body " + data, outfile, indent=1)
            outfile.write('\n')
            json.dump("Status Code :" + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 401, "Status code 401 expected in this case"
            outfile.close()
        else:
            break


@pytest.mark.security
def test_sync_with_GET_method():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        session = requests.session()
        outfile = getWriteFilePath("../sync_response_msg_file/" + list1[i] + "_sync_verify_with_GET_method_msg.json")
        response_api = session.get(set_properties_config()['API']['baseURI'] + set_properties_config()['API']['sync'],
                                   headers=set_api_header_text(list1[i]), )
        # response_api = set_api_get_method(setconfig()['API']['baseURI']e + setconfig()['API']['sync'],
        #                                   set_api_header("Lull"))
        respTime = str(round(response_api.elapsed.total_seconds(), 2))
        currDate = datetime.datetime.now()
        currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
        data = response_api.text
        outfile.write(list1[i] + " - Sync Endpoint -- Test Case: Test with GET method instead of the POST method")
        outfile.write(add_newline_text("API URL and the request header as follows:"))
        json.dump(response_api.request.url, outfile, indent=1)
        outfile.write('\n')
        json.dump(dict(response_api.request.headers), outfile, indent=2)
        outfile.write(add_newline_text("Response time information:"))
        json.dump(currDate + " " + respTime, outfile, indent=2)
        # outfile.write(add_newline_text("The request payload as follows:"))
        # json.dump(set_sync_json_payload("ec8055c82c9640638908891ca8587e74"), outfile, indent=1)
        outfile.write(add_newline_text("The response as follows:"))
        # outfile.write('\n')
        json.dump(data, outfile, indent=1)
        outfile.write("\n")
        json.dump("Status Code :" + str(response_api.status_code), outfile, indent=1)
        assert response_api.status_code == 405, "Status code 405 expected in this case"
        outfile.close()


@pytest.mark.security
def test_sync_with_application_text_instead_json():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        if list1[i] != 'Noretailer':
            lease_dict = lease_verify_before_sync(list1[i])
            time.sleep(5)
            outfile = getWriteFilePath("../sync_response_msg_file/" + list1[i] +
                                       "_sync_verify_with_application_text_response_msg.json")
            response_api = set_api_post_method(
                set_properties_config()['API']['baseURI'] + set_properties_config()['API']['sync'],
                set_api_header_text(list1[i]),
                set_sync_json_payload(str(lease_dict['uid'])))
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            data = response_api.json()
            outfile.write(
                list1[i] + " - Sync Endpoint -- Test Case: Test with application/text instead of application/json")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            json.dump(set_sync_json_payload(str(lease_dict['uid'])), outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            # outfile.write('\n')
            json.dump(data, outfile, indent=1)
            outfile.write("\n")
            json.dump("Status Code :" + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 500, "Status code 500 expected in this case"
            outfile.close()
        else:
            break

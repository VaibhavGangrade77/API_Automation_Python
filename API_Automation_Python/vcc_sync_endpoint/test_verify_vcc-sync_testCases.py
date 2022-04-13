import time

import pytest
import json
import datetime

from basic_utility_functions.api_header_utitlity import *
from basic_utility_functions.api_json_payload_utility import *
from basic_utility_functions.api_methods_utitlity import *
from basic_utility_functions.common_utility import *
from basic_utility_functions.file_operations_utility import *
from basic_utility_functions.get_api_response import get_sync_endpoint_response


@pytest.mark.security
def test_vcc_sync_with_valid_inputs():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        if list1[i] != 'Noretailer':
            sync_dict = get_sync_endpoint_response(list1[i])
            vcc_sync_uid = set_vcc_sync_json_payload(sync_dict['uid'])
            outfile = getWriteFilePath(
                "../vcc_sync_response_msg_file/" + list1[i] + "_vcc-sync_valid_response_msg.json")
            response_api = set_api_post_method(
                set_properties_config()['API']['baseURI'] + set_properties_config()['API']['vcc_sync'],
                set_api_header(list1[i]), vcc_sync_uid)
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            data = response_api.json()
            outfile.write(list1[i]+" -- VCC-Sync Endpoint -- Test Case: Test with all the valid details")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("Response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            json.dump(vcc_sync_uid, outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            # outfile.write('\n')
            json.dump(data, outfile, indent=1)
            outfile.write("\n")
            json.dump("Status Code :" + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 200, "Status code 200 expected in this case"
            outfile.close()
        else:
            break


@pytest.mark.security
def test_vcc_sync_with_wrong_URL_path():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        if list1[i] != 'Noretailer':
            sync_dict = get_sync_endpoint_response(list1[i])
            vcc_sync_uid = set_vcc_sync_json_payload(sync_dict['uid'])
            outfile = getWriteFilePath("../vcc_sync_response_msg_file/" + list1[i] + "_vcc-sync_with_wrong_URL_path_msg.json")
            response_api = set_api_post_method(
                set_properties_config()['API']['baseURI'] + set_properties_config()['API']['vcc_sync_v1'],
                set_api_header(list1[i]),
                set_vcc_sync_json_payload(vcc_sync_uid))
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            data = response_api.text
            outfile.write(list1[i]+" -- VCC-Sync Endpoint -- Test Case: Verify the response with wrong URL path")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("Response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            json.dump(vcc_sync_uid, outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            # outfile.write('\n')
            json.dump(data, outfile, indent=1)
            outfile.write("\n")
            json.dump("Status Code :" + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 404, "Status code 404 expected in this case"
            outfile.close()
        else:
            break


@pytest.mark.security
def test_vcc_sync_with_invalid_UID():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        if list1[i] != 'Noretailer':
            sync_dict = get_sync_endpoint_response(list1[i])
            vcc_sync_uid = set_vcc_sync_json_payload(sync_dict['uid']+'abcdef')
            time.sleep(3)
            outfile = getWriteFilePath("../vcc_sync_response_msg_file/" + list1[i] +
                                       "_vcc-sync_with_invalid_UID_msg.json")
            response_api = set_api_post_method(
                set_properties_config()['API']['baseURI'] + set_properties_config()['API']['vcc_sync'],
                set_api_header(list1[i]), vcc_sync_uid)
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            data = response_api.json()
            outfile.write(list1[i]+" -- VCC-Sync Endpoint -- Test Case: Test with the invalid UID")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("Response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            json.dump(vcc_sync_uid, outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            # outfile.write('\n')
            json.dump(data, outfile, indent=1)
            outfile.write("\n")
            json.dump("Status Code :" + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 400, "Status code 400 expected in this case"
            outfile.close()
        else:
            break


@pytest.mark.security
def test_vcc_sync_with_GET_instead_POST_method():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        if list1[i] != 'Noretailer':
            outfile = getWriteFilePath("../vcc_sync_response_msg_file/" + list1[i] + "_vcc-sync_with_GET_method_msg.json")
            response_api = set_api_get_method(
                set_properties_config()['API']['baseURI'] + set_properties_config()['API']['vcc_sync'],
                set_api_header(list1[i]))
            # response_api = set_api_post_method(setconfig()['API']['baseURI'] + setconfig()['API']['vcc_sync'],
            #                                    set_api_header("Lull"),
            #                                    set_no_payload())
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            data = response_api.text
            outfile.write(list1[i]+" -- VCC-Sync Endpoint -- Test Case: Test with the GET instead of POST method")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("Response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            json.dump(set_api_header(list1[i]), outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            # outfile.write('\n')
            json.dump(data, outfile, indent=1)
            outfile.write("\n")
            json.dump("Status Code :" + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 405, "Status code 405 expected in this case"
            outfile.close()
        else:
            break


@pytest.mark.security
def test_vcc_sync_without_payload():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        if list1[i] != 'Noretailer':
            outfile = getWriteFilePath("../vcc_sync_response_msg_file/" + list1[i] +
                                       "_vcc-sync_without_payload_response_msg.json")
            response_api = set_api_post_method(
                set_properties_config()['API']['baseURI'] + set_properties_config()['API']['vcc_sync'],
                set_api_header(list1[i]),
                set_no_payload())
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            data = response_api.json()
            outfile.write(list1[i]+" -- VCC-Sync Endpoint -- Test Case: Test without any JSON payload")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("Response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            json.dump(set_no_payload(), outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            # outfile.write('\n')
            json.dump(data, outfile, indent=1)
            outfile.write("\n")
            json.dump("Status Code :" + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 400, "Status code 400 expected in this case"
            outfile.close()
        else:
            break


@pytest.mark.security
def test_vcc_sync_remove_bearer_text():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        if list1[i] != 'Noretailer':
            sync_dict = get_sync_endpoint_response(list1[i])
            vcc_sync_uid = set_vcc_sync_json_payload(sync_dict['uid'])
            outfile = getWriteFilePath("../vcc_sync_response_msg_file/" + list1[i] +
                                       "_vcc-sync_remove_bearer_text_response_msg.json")
            response_api = set_api_post_method(
                set_properties_config()['API']['baseURI'] + set_properties_config()['API']['vcc_sync'],
                set_api_header_remove_Bearer(list1[i]), vcc_sync_uid)
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            data = response_api.text
            outfile.write(list1[i]+" -- VCC-Sync Endpoint -- Test Case: "
                                   "Removing the Bearer text from the authorization header")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("Response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            json.dump(set_api_header_remove_Bearer(list1[i]), outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            # outfile.write('\n')
            json.dump(data, outfile, indent=1)
            outfile.write("\n")
            json.dump("Status Code :" + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 401, "Status code 401 expected in this case"
            outfile.close()
        else:
            break


@pytest.mark.security
def test_vcc_sync_with_wrong_auth_code():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        if list1[i] != 'Noretailer':
            outfile = getWriteFilePath(
                "../vcc_sync_response_msg_file/Noretailer_vcc-sync_wrong_auth_code_response_msg.json")
            response_api = set_api_post_method(
                set_properties_config()['API']['baseURI'] + set_properties_config()['API']['vcc_sync'],
                set_api_header(list1[i]), set_vcc_sync_json_payload("a5c1d2691eec4cc9bf2cd919f00cb1"))
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            data = response_api.json()
            outfile.write("Noretailer -- VCC-Sync Endpoint -- Test Case: Test with wrong authorization code")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("Response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            json.dump(set_vcc_sync_json_payload("a5c1d2691eec4cc9bf2cd919f00cb1"), outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            # outfile.write('\n')
            json.dump(data, outfile, indent=1)
            outfile.write("\n")
            json.dump("Status Code :" + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 400, "Status code 400 expected in this case"
            outfile.close()


@pytest.mark.security
def test_vcc_sync_with_HTTP_instead_HTTPS():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        if list1[i] != 'Noretailer':
            sync_dict = get_sync_endpoint_response(list1[i])
            vcc_sync_uid = set_vcc_sync_json_payload(sync_dict['uid'])
            outfile = getWriteFilePath("../vcc_sync_response_msg_file/" + list1[i] +
                                       "_vcc_sync_verify_http_instead_https_msg.json")
            response_api = set_api_post_method(
                set_properties_config()['API']['http_baseURI'] + set_properties_config()['API']['vcc_sync'],
                set_api_header(list1[i]), vcc_sync_uid)
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            # response_api.raise_for_status()
            data = response_api.text
            outfile.write(list1[i]+" -- VCC-Sync Endpoint -- Test Case: Test with HTTP instead of the HTTPS protocol")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("Response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write("The Response as follows :")
            json.dump(data, outfile, indent=1)
            # json.dump(data, outfile, indent=1)
            outfile.write("\n")
            json.dump("Status Code :" + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 405, "Status code 405 expected in this case"
            outfile.close()
        else:
            break

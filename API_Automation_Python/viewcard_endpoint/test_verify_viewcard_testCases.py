import time

import pytest
import json
import datetime

from basic_utility_functions.api_header_utitlity import *
from basic_utility_functions.api_json_payload_utility import *
from basic_utility_functions.api_methods_utitlity import *
from basic_utility_functions.common_utility import *
from basic_utility_functions.file_operations_utility import *
from basic_utility_functions.get_api_response import get_vcc_sync_endpoint_response


@pytest.mark.security
def test_viewcard_with_valid_inputs():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        if list1[i] != 'Noretailer':
            dict_token = get_vcc_sync_endpoint_response(list1[i])
            viewcard_auth = set_viewcard_authcode(dict_token['token'])
            outfile = getWriteFilePath("../viewcard_response_msg_file/" + list1[i] +
                                       "_viewcard_valid_response_msg.json")
            response_api = set_api_post_method(
                set_properties_config()['API']['api_base_uri'] + set_properties_config()['API']['viewcard'],
                viewcard_auth, set_no_payload())
            data = response_api.text
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            outfile.write(list1[i] + " - View Card Endpoint -- Test Case: Test with all the valid details")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            json.dump('{}', outfile, indent=1)
            outfile.write("\n")
            json.dump("Request Method :" + response_api.request.method, outfile, indent=1)
            outfile.write("\n")
            json.dump(viewcard_auth, outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            # outfile.write('\n')
            json.dump(data, outfile, indent=1)
            outfile.write("\n")
            json.dump("Status Code :" + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 200, "Status code 200 expected in this case"
            outfile.close()


@pytest.mark.security
def test_viewcard_with_http_instead_https():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        if list1[i] != 'Noretailer':
            dict_token = get_vcc_sync_endpoint_response(list1[i])
            viewcard_auth = set_viewcard_authcode(dict_token['token'])
            outfile = getWriteFilePath("../viewcard_response_msg_file/" + list1[i] +
                                       "_viewcard_verify_with_http_instead_https_msg.json")
            response_api = set_api_post_method(set_properties_config()['API']['http_api_base_uri'] +
                                               set_properties_config()['API']['viewcard'],
                                               viewcard_auth,
                                               set_no_payload())
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            data = response_api.text
            outfile.write(list1[i] + " - VCC-Sync Endpoint -- Test Case: Test with HTTP instead of the HTTPS")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            outfile.write("\n")
            json.dump("Request Method :" + response_api.request.method, outfile, indent=1)
            json.dump(viewcard_auth, outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            # outfile.write('\n')
            json.dump(data, outfile, indent=1)
            outfile.write("\n")
            json.dump("Status Code :" + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 200, "Status code 200 expected in this case"
            outfile.close()


@pytest.mark.security
def test_viewcard_with_invalid_auth_code():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, 2):
        if list1[i] != 'Noretailer':
            dict_token = get_vcc_sync_endpoint_response(list1[i])
            viewcard_auth = set_viewcard_authcode(str(dict_token['token']) + 'abcde')
            outfile = getWriteFilePath("../viewcard_response_msg_file/" + list1[i] +
                                       " - viewcard_verify_with_invalid_auth_code_msg.json")
            response_api = set_api_post_method(set_properties_config()['API']['api_base_uri'] +
                                               set_properties_config()['API']['viewcard'],
                                               viewcard_auth,
                                               set_no_payload())
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()

            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            data = response_api.text
            outfile.write(list1[i] + " - VCC-Sync Endpoint -- Test Case: Test with the invalid authorization code")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            outfile.write("\n")
            json.dump("Request Method :" + response_api.request.method, outfile, indent=1)
            json.dump(viewcard_auth, outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            # outfile.write('\n')
            json.dump(data, outfile, indent=1)
            outfile.write("\n")
            json.dump("Status Code :" + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 403, "Status code 403 expected in this case"
            outfile.close()


@pytest.mark.security
def test_viewcard_remove_text_bearer():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, 2):
        if list1[i] != 'Noretailer':
            dict_token = get_vcc_sync_endpoint_response(list1[i])
            viewcard_auth = set_viewcard_remove_bearer(dict_token['token'])
            outfile = getWriteFilePath("../viewcard_response_msg_file/" + list1[i] +
                                       " - viewcard_remove_text_bearer_auth_msg.json")
            response_api = set_api_post_method(
                set_properties_config()['API']['api_base_uri'] + set_properties_config()['API']['viewcard'],
                viewcard_auth,
                set_no_payload())
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()

            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            data = response_api.text
            outfile.write(list1[i] +
                          "- VCC-Sync Endpoint -- Test Case: Test with by removing the text Bearer from Authorization "
                          "header")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            outfile.write("\n")
            json.dump("Request Method :" + response_api.request.method, outfile, indent=1)
            json.dump(viewcard_auth, outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            # outfile.write('\n')
            json.dump(data, outfile, indent=1)
            outfile.write("\n")
            json.dump("Status Code :" + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 500, "Status code 500 expected in this case"
            outfile.close()


@pytest.mark.security
def test_viewcard_use_GET_instead_POST():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, 2):
        if list1[i] != 'Noretailer':
            dict_token = get_vcc_sync_endpoint_response(list1[i])
            viewcard_auth = set_viewcard_authcode(str(dict_token['token']))
            outfile = getWriteFilePath("../viewcard_response_msg_file/" + list1[i] +
                                       " - viewcard_use_get_instead_post_msg.json")
            response_api = set_api_get_method(set_properties_config()['API']['api_base_uri'] +
                                              set_properties_config()['API']['viewcard'],
                                              viewcard_auth)
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            data = response_api.text
            outfile.write(list1[i] +
                          " - VCC-Sync Endpoint -- Test Case: Test with the GET method instead of the POST method")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            outfile.write("\n")
            json.dump("Request Method :" + response_api.request.method, outfile, indent=1)
            json.dump(viewcard_auth, outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            # outfile.write('\n')
            json.dump(data, outfile, indent=1)
            outfile.write("\n")
            json.dump("Status Code :" + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 403, "Status code 403 expected in this case"
            outfile.close()


@pytest.mark.security
def test_viewcard_with_expired_authcode():
    outfile = getWriteFilePath("../viewcard_response_msg_file/viewcard_with_expired_authcode_msg.json")
    viewcard_auth = 'eyJhbGciOiJSUzUxMiIsImtpZCI6IjEyMzQ1Njc4OTAiLCJ0eXAiOiJKV1QifQ.eyJhcHBfaWQiOjIyMjksInJldGFpbGVyX2lkIjoyOSwiaXNzIjoia3RwbHRfSldUIiwiZXhwIjoxNjI4ODU5NDI0LCJpYXQiOjE2Mjg4NDg2MjQsInNjb3BlIjoidmNjLWp3dC1hcGkvVmlld0NhcmQifQ.IQicNmRAy0NQhlhTZUYV7VBXZEGZE5EszsYG-BYYkGl0tKgsMzSsuIOEbckKOw8wakAvUb5EWDEnLbuIZVKGoocdpWrdv2lNd37P-FPIUN7fZ0GODNdNi0sgEkYpqOJuytcjAmTkYfear_BecJ4PoebR_GUbhmY8x2UBc2N3Y9YlkPjxUWb6Deyznx3rNImDy88dOXC0X_fHJFzXFaBlemnXbf84LDZrHMWdo0WiRKPWgld3EJBPbVjr9dKzkg2SGBR80z-8v07QdIfzYg_7W0wkNiOK5ycRjy0Uh9DEaSudkNerwP-qi8tr27Eo2zNi7WDSAiLBW1NWFekzGEwnMqlCcLTNcdrw-Xaj3pxMQ-m8ur9nMRNNIueEj_1iKWXbRLqe5fiGpRrkc48RtwJW3TnpJOtveIr6omrJyqMPd-qFl25ybguA7s6Qq9oYAcypWK56etR22rCIyL6wDCluduRMbS4mRL9rupwXf4-j4VrR0VpqddO-Hybgo2yn2ATVSsj8wozt9N9acbypQDmL4c819saVG4F3v0rMADWQq35Vbk_Cer3Jf2pxKr35Z4hA7KeBQbfKdopUK9zmJwZ6ZKArLQmsByMOyBcuyIZlkgT75AuX1vmSQ3DgfeI5Gija5BnpUT1wqe_UrlE8DJurr21ZSqRDor56SB5Rb5m12A4'
    response_api = set_api_post_method(
        set_properties_config()['API']['api_base_uri'] + set_properties_config()['API']['viewcard'],
        set_viewcard_authcode(viewcard_auth),
        set_no_payload())
    respTime = str(round(response_api.elapsed.total_seconds(), 2))
    currDate = datetime.datetime.now()

    currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
    data = response_api.text
    outfile.write("VCC-Sync Endpoint -- Test Case: Test with the expired auth code in the authorization header")
    outfile.write(add_newline_text("API URL and the request header as follows:"))
    json.dump(response_api.request.url, outfile, indent=1)
    outfile.write('\n')
    json.dump(dict(response_api.request.headers), outfile, indent=2)
    outfile.write(add_newline_text("response time information:"))
    json.dump(currDate + " " + respTime, outfile, indent=2)
    outfile.write(add_newline_text("The request payload as follows:"))
    outfile.write("\n")
    json.dump("Request Method :" + response_api.request.method, outfile, indent=1)
    json.dump(set_viewcard_authcode(viewcard_auth), outfile, indent=1)
    outfile.write(add_newline_text("The response as follows:"))
    # outfile.write('\n')
    json.dump(data, outfile, indent=1)
    outfile.write("\n")
    json.dump("Status Code :" + str(response_api.status_code), outfile, indent=1)
    assert response_api.status_code == 403, "Status code 403 expected in this case"
    outfile.close()

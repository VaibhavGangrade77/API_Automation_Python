import json
import pytest
import datetime

from basic_utility_functions.api_header_utitlity import set_api_header, set_retailer_list, set_api_header_remove_Bearer
from basic_utility_functions.api_json_payload_utility import set_isleasable_json_payload
from basic_utility_functions.api_methods_utitlity import set_api_get_method, set_api_post_method
from basic_utility_functions.common_utility import set_properties_config, add_newline_text
from basic_utility_functions.file_operations_utility import getWriteFilePath

"""RL = retailer_lookup"""


@pytest.mark.security
def test_RL_with_valid_inputs():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        if list1[i] != 'Noretailer':
            response_api = set_api_get_method(
                set_properties_config()['API']['baseURI'] + set_properties_config()['API']['retailer_lookup'],
                set_api_header(list1[i]))
            outfile = getWriteFilePath(
                "../retailer_lookup_response_msg_file/" + list1[i] +
                "_RL_verify_with_valid_input_response_msg.json")
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            data = response_api.json()
            outfile.write(list1[i]+" -- Retailer Lookup Endpoint -- Test Case: Test with valid Inputs")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            json.dump(set_api_header(list1[i]), outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            json.dump(data, outfile, indent=1)
            outfile.write("\n")
            json.dump("Status Code :" + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 202, "Status code 202 expected in this case"
            outfile.close()


@pytest.mark.security
def test_RL_with_HTTP_instead_HTTPS():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        if list1[i] != 'Noretailer':
            response_api = set_api_get_method(
                set_properties_config()['API']['http_baseURI'] + set_properties_config()['API']['retailer_lookup'],
                set_api_header(list1[i]))
            outfile = getWriteFilePath("../retailer_lookup_response_msg_file/" + list1[i] +
                                       "_RL_http_instead_HTTPS_response_msg.json")
            respTime = str(round(response_api.elapsed.total_seconds(), 2))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            data = response_api.json()
            outfile.write(list1[i] + " --Retailer Lookup Endpoint -- Test Case: Test with HTTP instead of the HTTPS")
            outfile.write(add_newline_text("API URL and the request header as follows:"))
            json.dump(response_api.request.url, outfile, indent=1)
            outfile.write('\n')
            json.dump(dict(response_api.request.headers), outfile, indent=2)
            outfile.write(add_newline_text("response time information:"))
            json.dump(currDate + " " + respTime, outfile, indent=2)
            outfile.write(add_newline_text("The request payload as follows:"))
            json.dump(set_api_header(list1[i]), outfile, indent=1)
            outfile.write(add_newline_text("The response as follows:"))
            json.dump(data, outfile, indent=1)
            outfile.write("\n")
            json.dump("Status Code :" + str(response_api.status_code), outfile, indent=1)
            assert response_api.status_code == 202, "Status code 202 expected in this case"
            outfile.close()


@pytest.mark.security
def test_RL_with_invalid_bearer_token():
    response_api = set_api_get_method(
        set_properties_config()['API']['baseURI'] + set_properties_config()['API']['retailer_lookup'],
        set_api_header("Noretailer"))
    outfile = getWriteFilePath(
        "../retailer_lookup_response_msg_file/RL_verify_with_invalid_bearer_token_response_msg.json")
    respTime = str(round(response_api.elapsed.total_seconds(), 2))
    currDate = datetime.datetime.now()
    currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
    data = response_api.text
    outfile.write("NoRetailer -- Retailer Lookup Endpoint -- Test Case: Test with invalid bearer token")
    outfile.write(add_newline_text("API URL and the request header as follows:"))
    json.dump(response_api.request.url, outfile, indent=1)
    outfile.write('\n')
    json.dump(dict(response_api.request.headers), outfile, indent=2)
    outfile.write(add_newline_text("response time information:"))
    json.dump(currDate + " " + respTime, outfile, indent=2)
    outfile.write(add_newline_text("The request payload as follows:"))
    json.dump(set_api_header('Noretailer'), outfile, indent=1)
    outfile.write(add_newline_text("The response as follows:"))
    # outfile.write('\n')
    json.dump(data, outfile, indent=1)
    outfile.write("\n")
    json.dump("Status Code :" + str(response_api.status_code), outfile, indent=1)
    assert response_api.status_code == 401, "Status code 401 expected in this case"
    outfile.close()


@pytest.mark.security
def test_RL_with_remove_bearer_text():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        response_api = set_api_get_method(
            set_properties_config()['API']['baseURI'] + set_properties_config()['API']['retailer_lookup'],
            set_api_header_remove_Bearer(list1[i]))
        outfile = getWriteFilePath(
            "../retailer_lookup_response_msg_file/" + list1[i] + "_RL_verify_with_remove_bearer_text_msg.json")
        respTime = str(round(response_api.elapsed.total_seconds(), 2))
        currDate = datetime.datetime.now()
        currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
        data = response_api.text
        outfile.write(list1[i] + "--Retailer Lookup Endpoint -- Test Case: Test with remove the Bearer text from the "
                                 "Authorization")
        outfile.write(add_newline_text("API URL and the request header as follows:"))
        json.dump(response_api.request.url, outfile, indent=1)
        outfile.write('\n')
        json.dump(dict(response_api.request.headers), outfile, indent=2)
        outfile.write(add_newline_text("response time information:"))
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


@pytest.mark.security
def test_RL_with_POST_instead_GET():
    list1 = set_retailer_list(int(set_properties_config()['COLUMNS']['col1']))
    for i in range(1, len(list1)):
        outfile = getWriteFilePath(
            "../retailer_lookup_response_msg_file/" + list1[i] + "_RL_verify_with_post_instead_get_method_msg.json")
        response_api = set_api_post_method(
            set_properties_config()['API']['baseURI'] + set_properties_config()['API']['retailer_lookup'],
            set_api_header(list1[i]),
            set_isleasable_json_payload("Mattress"))

        respTime = str(round(response_api.elapsed.total_seconds(), 2))
        currDate = datetime.datetime.now()
        currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
        data = response_api.text
        outfile.write(list1[i] + "--Retailer Lookup Endpoint -- Test Case: Test with POST method instead of the GET "
                                 "method")
        outfile.write(add_newline_text("API URL and the request header as follows:"))
        json.dump(response_api.request.url, outfile, indent=1)
        outfile.write('\n')
        json.dump(dict(response_api.request.headers), outfile, indent=2)
        outfile.write(add_newline_text("response time information:"))
        json.dump(currDate + " " + respTime, outfile, indent=2)
        outfile.write(add_newline_text("The request payload as follows:"))
        json.dump(set_api_header(list1[i]), outfile, indent=1)
        outfile.write(add_newline_text("The response as follows:"))
        json.dump(data, outfile, indent=1)
        outfile.write("\n")
        json.dump("Status Code :" + str(response_api.status_code), outfile, indent=1)
        assert response_api.status_code == 405, "Status code 405 expected in this case"
        outfile.close()

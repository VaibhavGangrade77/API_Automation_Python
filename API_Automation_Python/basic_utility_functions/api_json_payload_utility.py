def set_isleasable_json_payload(param_val):
    set_json = {"item_display_name": param_val}
    return set_json


def set_sync_json_payload(param_val):
    set_json = {"order_id": "null", "uid": param_val}
    return set_json


def set_no_payload():
    set_json = {}
    return set_json


def set_vcc_sync_json_payload(param_val):
    set_vcc_json = {"uid": param_val}
    return set_vcc_json


def set_req_ver_json_payload(phone_num):
    set_phone = {"phone": phone_num}
    return set_phone


def set_verification_json_payload(phone_num):
    set_code = {"code": "323242", "last_four": "3434", "phone": phone_num}
    return set_code


def set_address_chk_json_payload(phone_num):
    set_code = {"customer": {"shipping": {"first_name": "Mclauren o.", "middle_name": "", "last_name": "Keating",
                                          "address": "790 Mcdougald St", "address2": "", "city": "GENEVA",
                                          "state": "AL", "country": "United States", "zip": "36340",
                                          "email": "lauren9898@gmail.com", "phone": "(334) 792 6895"},
                             "billing": {"first_name": "Mclauren o.", "middle_name": "", "last_name": "Keating",
                                         "address": "790 Mcdougald St", "address2": "", "city": "GENEVA", "state": "AL",
                                         "country": "United States", "zip": "36340", "email": "lauren9898@gmail.com",
                                         "phone": "(334) 792 6895"}}, "items": [
        {"display_name": "razr (2nd Gen) Polished Graphite - 256GB", "sku": "razr (2nd Gen) Polished Graphite - 256GB",
         "unit_price": 799.99, "quantity": 2, "leasable": True},
        {"display_name": "Touch Screen Stylus Pen (2021) - White - for moto g stylus 2021",
         "sku": "Touch Screen Stylus Pen (2021) - White - for moto g stylus 2021", "unit_price": 19.99, "quantity": 5,
         "leasable": True},
        {"display_name": "motorola one 5G ace 6+128 Frosted Silver", "sku": "motorola one 5G ace 6+128 Frosted Silver",
         "unit_price": 299.99, "quantity": 1, "leasable": False}],
                "checkout": {"customer_id": "null", "shipping_amount": 0,
                             "discounts": [{"discount_name": "Total Savings", "discount_amount": 0}]}, "sales_tax": 190,
                "cart_total": 2189.92, "urls": {"return": False, "cancel": False}, "phone": phone_num,
                "code": "323242"}
    return set_code


def set_cart_chk_json_payload(phone_num):
    set_code = {"customer": {"shipping": {"first_name": "Mclauren o.", "middle_name": "", "last_name": "Keating",
                                          "address": "790 Mcdougald St", "address2": "", "city": "GENEVA",
                                          "state": "AL", "country": "United States", "zip": "36340",
                                          "email": "lauren9898@gmail.com", "phone": "(334) 792 6895"},
                             "billing": {"first_name": "Mclauren o.", "middle_name": "", "last_name": "Keating",
                                         "address": "790 Mcdougald St", "address2": "", "city": "GENEVA", "state": "AL",
                                         "country": "United States", "zip": "36340", "email": "lauren9898@gmail.com",
                                         "phone": "(334) 792 6895"}}, "items": [
        {"display_name": "razr (2nd Gen) Polished Graphite - 256GB", "sku": "razr (2nd Gen) Polished Graphite - 256GB",
         "unit_price": 799.99, "quantity": 2, "leasable": True},
        {"display_name": "Touch Screen Stylus Pen (2021) - White - for moto g stylus 2021",
         "sku": "Touch Screen Stylus Pen (2021) - White - for moto g stylus 2021", "unit_price": 19.99, "quantity": 5,
         "leasable": True},
        {"display_name": "motorola one 5G ace 6+128 Frosted Silver", "sku": "motorola one 5G ace 6+128 Frosted Silver",
         "unit_price": 299.99, "quantity": 1, "leasable": False}],
                "checkout": {"customer_id": "null", "shipping_amount": 0,
                             "discounts": [{"discount_name": "Total Savings", "discount_amount": 0}]}, "sales_tax": 190,
                "cart_total": 2189.92, "urls": {"return": False, "cancel": False}, "phone": phone_num, "code": "323242",
                "new_address": False}
    return set_code


def set_initialize_json_payload(phone_num):
    set_code = {"customer": {"shipping": {"first_name": "Mclauren o.", "middle_name": "", "last_name": "Keating",
                                          "address": "790 Mcdougald St", "address2": "", "city": "GENEVA",
                                          "state": "AL", "country": "United States", "zip": "36340",
                                          "email": "lauren9898@gmail.com", "phone": "(334) 792 6895"},
                             "billing": {"first_name": "Mclauren o.", "middle_name": "", "last_name": "Keating",
                                         "address": "790 Mcdougald St", "address2": "", "city": "GENEVA", "state": "AL",
                                         "country": "United States", "zip": "36340", "email": "lauren9898@gmail.com",
                                         "phone": "(334) 792 6895"}}, "items": [
        {"display_name": "razr (2nd Gen) Polished Graphite - 256GB", "sku": "razr (2nd Gen) Polished Graphite - 256GB",
         "unit_price": 799.99, "quantity": 2, "leasable": True},
        {"display_name": "Touch Screen Stylus Pen (2021) - White - for moto g stylus 2021",
         "sku": "Touch Screen Stylus Pen (2021) - White - for moto g stylus 2021", "unit_price": 19.99, "quantity": 5,
         "leasable": True},
        {"display_name": "motorola one 5G ace 6+128 Frosted Silver", "sku": "motorola one 5G ace 6+128 Frosted Silver",
         "unit_price": 299.99, "quantity": 1, "leasable": False}],
                "checkout": {"customer_id": "null", "shipping_amount": 0,
                             "discounts": [{"discount_name": "Total Savings", "discount_amount": 0}]}, "sales_tax": 190,
                "cart_total": 2189.92, "urls": {"return": False, "cancel": False}, "phone": phone_num, "code": "323242",
                "new_address": False}

    return set_code


def set_contract_json_payload(uid):
    set_code = {"application_id": uid}
    return set_code


def set_first_payment_json_payload():
    set_code = {"payment_details": {"CardNumber": "4111111111111111", "CardExpiration": "03/23", "CardCvv": "123",
                                    "Contract": "true", "Disclosure": "true", "PaymentType": "debit"}}
    return set_code

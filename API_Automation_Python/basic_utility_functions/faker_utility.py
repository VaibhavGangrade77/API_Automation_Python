from faker import Faker


def get_user_name():
    return Faker.name()


def get_user_address():
    return Faker.address()


def get_user_email():
    return Faker.email()


def get_user_ssn():
    return Faker.ssn()


def get_user_birthdate():
    return Faker.birthdate()


def get_user_profile():
    return Faker.profile()


def get_first_name():
    return Faker.first_name()


def get_lat_name():
    return Faker.last_name()


def get_phone_number():
    return Faker.numerify()


def get_pay_date():
    return Faker.date_this_month()

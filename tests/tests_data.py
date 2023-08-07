from faker import Faker

class Invalid_Data:
    fake_email = Faker().email()
    fake_password = Faker().password()
    fake_name = Faker().name()
    first_name_1_char = 'П'
    first_name_31_char = 'Петртртртртртртртртртртртртртрт'
    last_name_1_char = 'П'
    last_name_31_char = 'Петртртртртртртртртртртртртртрт'
    password_21_char = 'Qwerty0Qwerty0Qwerty0'
    password_no_Lower = 'qwertyu0'
    password_9_char = 'Qwertyu0p'
    password_4_char = 'qwer'
    password_not_contain_digit = "Qwertyui"
    email_without_domain = '12345@.ru'
    invalid_phoneNumber = '+79999999999'

class Valid_Data:
    valid_first_name = 'Петр'
    valid_last_name = 'Петров'
    valid_password = 'Qwert123Qwerty'
    valid_phoneNumber = '+79328636673'
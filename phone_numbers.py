#Import the 'phonenumbers' module for working with phone numbers
import phonenumbers
import wikipedia
import os
def phone_number(number,country_code):
    #Define a phone number string that you want to check for validity
    phone_number_str = (f"{number}+{country_code}")
    
    #Parse the phone number string into a Phonenumber object using the 'parse' function
    parsed_phone_number = phonenumbers.parse(phone_number_str)

    #check if the parsed phone number is valid using the 'is_valid_number' function
    is_valid = phonenumbers.is_valid_number(parsed_phone_number)

    #Get information about the country that the phone number belongs to using the 'region _code' function
    country_code_ = phonenumbers.region_code_for_number(parsed_phone_number)

    #Get the type of the phone number(e.g., MOBILE, FIXED_LINE) using the 'number_type' functions
    number_type = phonenumbers.number_type(parsed_phone_number)

    #Format the phone number in various formats using the 'format_number' function
    formatted_international = phonenumbers.format_number(parsed_phone_number,phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    formatted_national = phonenumbers.format_number(parsed_phone_number,phonenumbers.PhoneNumberFormat.NATIONAL)
    formatted_e164 = phonenumbers.format_number(parsed_phone_number,phonenumbers.PhoneNumberFormat.E164)

    #Get more information about the phone number using additional functions
    national_significant_number = phonenumbers.national_significant_number(parsed_phone_number)


    #print detailed information about the phone number
    print(f"Original Phone Number:{phone_number_str}")
    print(f"Parsed Phone Number:{parsed_phone_number}")
    print(f"Is Valid:{is_valid}")
    print(f"Country code:{country_code_}")
    print(f"Number Type:{number_type}")
    print(f"National Significant Number:{national_significant_number}")
    print(f"Formatted International:{formatted_international}")
    print(f"Formatted National:{formatted_national}")
    print(f"Formatted E164:{formatted_e164}")

    #print a final result indicating whether the phone number is valid or  not
    if is_valid:
        print("The provided phone number is valid.")
        return "valid"
    else:
        print("The provided phone number is not valid.")
        return "invalid"
    
phone_number("9081282794","91")

import phonenumbers as ph
from phonenumbers import geocoder

number = "+917479555689"
parsed_number = ph.parse(number)

country_code = geocoder.region_code_for_number(parsed_number)

print("Country Code:", country_code)

state_info = {
    "IN": "India",
    
}

print("State:", state_info.get(country_code, "State information not available"))

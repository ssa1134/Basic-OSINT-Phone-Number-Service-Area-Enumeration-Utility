import phonenumbers
from phonenumbers import geocoder
phone_number1=phonenumbers.parse("+917009262789")
phone_number2=phonenumbers.parse("+918288933544")
phone_number3=phonenumbers.parse("+919805806458")
phone_number4=phonenumbers.parse("+919780015100")

print("\nPhone numbers Location\n")
print(geocoder.description_for_number(phone_number1,"en"))
print(geocoder.description_for_number(phone_number2,"en"))
print(geocoder.description_for_number(phone_number3,"en"))
print(geocoder.description_for_number(phone_number4,"en"))

# LETS TRACK THE PHONE NUMBERS
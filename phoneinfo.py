import phonenumbers

from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
from datetime import datetime
 

number = input("Enter a phone number: ")


try:
            phone_number = phonenumbers.parse(number, "GR")

            print("Number: ", number)
            print("Country or City: ", geocoder.description_for_number(phone_number, "en")) #prints the Country (or the City if it is a home phone number) in which the number is registered
                                                
            service_number = phonenumbers.parse(number, "GR")

            print("Carrier: ", carrier.name_for_number(service_number, "en")) #prints the carrier of the phone number (It works with mobile numbers)
                                                
            phone_number = phonenumbers.parse(number, "GR")
                                    
            print("Timezone :", timezone.time_zones_for_number(phone_number)) #print the timezone that the number belongs

            phone_number = phonenumbers.parse(number)
                                    
            valid = phonenumbers.is_valid_number(phone_number) #checks if it is a valid phone number
            possible = phonenumbers.is_valid_number(phone_number) #checks if it is a possible phone number

            if valid==True and possible==True:
                print("This is a valid and possible phone number")
                                    
            else:
                print("This is not a valid phone number (Note: Potentially dangerous phone number)")
            now = datetime.now()
            date_str = now.strftime("%d/%m/%Y %H:%M:%S")
            print("Date and time of searching:", date_str) #prints the date and the time of searching

                                    
except Exception:
    print("Error!")
    print("Country or city not found")
    print("Carrier not found")

try:
    from googlesearch import search
except ImportError:
    print("No results found")

print("_______________", "***************", "_______________", "***************", sep="\n")

# to search
query = number
 
for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)    




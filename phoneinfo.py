#mrpol#

import phonenumbers

from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
from datetime import datetime

#Ask the user if he wants info about a phone number
question = input("Do you want info about a phone number? (y/n): ")
check = True

while check == True:

    if question=="y":
            
        check = False
        device = input("Do you want info about a Mobile phone or Home phone number? (m/h): ")   #Ask the type of the phone number in order to print the right note
            
        if device == "h":
            print("Note: Carrier cannot be found")
                
        elif device == "m":
            print("Note: Carrier can be found")
                
        else:
            break
                    
        number = input("Enter a phone number: ") #Ask the phone number (The number which is given must start with the right country code (eg +30 for Greece, +34 for Spain, etc.)
                
        try:
            phone_number = phonenumbers.parse(number, "CH")

            print("Number: ", number)
            print("Country or City: ", geocoder.description_for_number(phone_number, "en")) #print the Country (or the City if it is a home phone numer) in which the number is registered
                                
            service_number = phonenumbers.parse(number, "RO")

            print("Carrier: ", carrier.name_for_number(service_number, "en")) #print the carrier of the phone number (It works with mobile numbers)
                                
            phone_number = phonenumbers.parse(number, "EU")
                    
            print("Timezone :", timezone.time_zones_for_number(phone_number)) #print the timezone that the number belongs

            phone_number = phonenumbers.parse(number)
                    
            valid = phonenumbers.is_valid_number(phone_number) #check if it is a valid phone number
            possible = phonenumbers.is_valid_number(phone_number) #check if it is a possible phone number

            if valid==True and possible==True:
                print("This is a valid and possible phone number") #print that it is a valid and a possible phone number
                    
            else:
                print("This is not a valid phone number (Note: Potentially dangerous phone number)") #print that it is not a valid phone number (potentially dangerous)

            now = datetime.now()
            date_str = now.strftime("%d/%m/%Y %H:%M:%S")
            print("Date and time of searching:", date_str) #print date and time of searching
                    
        except Exception:
            print("Error!")
            print("Country or city not found")
            print("Carrier not found")
            check = True
            q = input("Do you want to continue? (y/n): ")
                
            if q == "n":
                check = False
                print("Thanks, bye!")
            elif q == "y":
                check = True
            else:
                break

    elif question=="n":
        print("Sorry,I can't help you.")
        break
    else:
        break


    
    
        
            
    

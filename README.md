# phoneinfo

This is a python program which could be used as an information gathering tool about phone numbers.

This program gives info about a phone number which the user inputs (mobile phone number and home phone number).
It works succesfully with countries of different continents, but if not, maybe you have to make little changes in the second argument of the function parse, as it is specify the place that the phone number is being dialled from (unless the number is in E.164 format, which is globally unique). As a first option the second argument of parse is specified as "EU". 


# NOTE:

The program needs the country code in front of the phone number in order to work right. (eg +30 -> Greece, +34 -> Spain etc)


# Possibilities:

• Shows the country (or the city, if it is a home phone number) in which the phone number is registered.

• Shows the carrier (if it is a mobile phone number).

• Shows the timezone of the country/city in which the phone number is registered.

• Checks if the number that the user inputs is valid or registered (I also checked it with scam numbers and in this case, the program detects them and prints a warning message).

• Prints the date and the time of searching.

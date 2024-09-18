
import csv
from tabulate import tabulate
from emoji import emojize
import random
from colorama import Fore, Back, Style
from function import real_time_flight_info,seat_selection,class_selection,user_login,user_create, data_storage, item_check, loyalty,price, image_view
from function import bag_check
class users:    #used for the values of newly created users
    air_ontario = []
    paypal = []
    google_pay = []
    apple_pay = []

class stored_users(): # used for the values of already stored users 
    air_ontario = []
    paypal = []
    google_pay = []
    apple_pay = []

cities = ['regina','thunder bay','winnipeg','ottowa','yellow knife','pei','halifax','edmonton','hamilton','montreal','vancouver','calgary']



def main():

    flight_info = [f"{Style.BRIGHT}City","Flight Number","Terminal","Status","Time of departure","Time of arrival","Carousel Number","Desination Code"]
    regina =  [f"{Fore.BLUE}Regina",f"{Style.DIM}{Fore.WHITE}1265"," 01"] + real_time_flight_info() + ["01","543"]
    thunder_bay = [f"{Fore.CYAN}Thunder Bay",f"{Style.DIM}{Fore.WHITE}1111","00"] + real_time_flight_info() + ["02","534"]
    winnipeg= [f"{Fore.GREEN}Winnepeg",f"{Style.DIM}{Fore.WHITE}9000","02"] + real_time_flight_info() + ["17","253"]
    ottowa = [f"{Fore.LIGHTMAGENTA_EX}Ottowa",f"{Style.DIM}{Fore.WHITE}1089"," 06"] + real_time_flight_info() + ["10","686"]
    yellow_knife=[f"{Fore.WHITE}Yellow Knife",f"{Style.DIM}{Fore.WHITE}1766","04"] + real_time_flight_info() + ["03","575"]
    pei = [f"{Fore.RED}PEI",f"{Style.DIM}{Fore.WHITE}7894", "01",] + real_time_flight_info() + ["09","776"]
    halifax = [f"{Fore.LIGHTYELLOW_EX}Halifax", f"{Style.DIM}{Fore.WHITE}4444"," 03"] + real_time_flight_info() + ["07","521"]
    edmonton = [f"{Fore.LIGHTBLUE_EX}Edmonton",f"{Style.DIM}{Fore.WHITE}5674"," 02"] + real_time_flight_info() + ["10","474"]
    hamilton = [f"{Fore.LIGHTRED_EX}Hamilton",f"{Style.DIM}{Fore.WHITE}5555"," 00 "] + real_time_flight_info() + ["16","502"]
    montreal = [f"{Fore.BLACK}Montreal",f"{Style.DIM}{Fore.WHITE}1234","04"] + real_time_flight_info() + ["10","926"]
    vancouver= [f"{Fore.LIGHTGREEN_EX}Vancouver",f"{Style.DIM}{Fore.WHITE}4356","05"] + real_time_flight_info() + ["17","129"]
    calgary = [f"{Fore.YELLOW}Calgary", f"{Style.DIM}{Fore.WHITE}5567","00"] + real_time_flight_info() + ["19","425"]

    
#merging all the lists into an array 
    complete_list = [flight_info,regina,thunder_bay,winnipeg,ottowa,yellow_knife,pei,halifax,edmonton,hamilton,montreal,vancouver,calgary]
    print(tabulate(complete_list, tablefmt="modern"))
    print(Style.RESET_ALL,"")

# thank you message and meaning of status symbols

    print("Thank you for choosing Air Ontario")
    print(emojize(" -:red_circle: means the flight is cancelled"))
    print(emojize(" -:green_circle: means the flight is on time"))    
    print(emojize(" -:yellow_circle: means the flight is delayed"))
    print(emojize(" -:blue_circle: means the flight has arrived"))

    # here it will let users check the additional info of a flight

    image_view(cities)

    #here we will start letting the user do flight orders

    while True:
        _ = input("Would you like to purchase a flight?   ").strip().lower()

        if _  == "yes":
            break
    
        elif _ == "no":
            return None
    
        else:
            pass
# acceses stored files 
    stored_users.paypal = data_storage(users.paypal,'paypal.csv')
    stored_users.apple_pay = data_storage(users.apple_pay,'apple_pay.csv')
    stored_users.google_pay = data_storage(users.google_pay,'google_pay.csv')
    stored_users.air_ontario = data_storage(users.air_ontario,'air_ontario.csv')


    
# creates a new account if the user wants it, the  current values for the user class will be set to only newly created accounts
    user_create(users.paypal,"Paypal",stored_users.paypal)
    user_create(users.apple_pay,"Apple Pay",stored_users.apple_pay)
    user_create(users.google_pay,"Google Pay",stored_users.google_pay)
    user_create(users.air_ontario, "Air Ontario",stored_users.air_ontario)
    

    # stores data from newly created users and sets values for the user class as all stored values
    users.paypal = data_storage(users.paypal,'paypal.csv')
    users.apple_pay = data_storage(users.apple_pay,'apple_pay.csv')
    users.google_pay = data_storage(users.google_pay,'google_pay.csv')
    users.air_ontario = data_storage(users.air_ontario,'air_ontario.csv')
    payment_method = ""

# we need an air ontario account to be logged in
    current_air_ontario= user_login(users.air_ontario,"Air Ontario")
    
    # we input one of the input methods
    while True:
        payment_method = input("What is your payment method:  ").strip().lower()
        if payment_method == "google pay":
            user_login(users.google_pay,"Google Pay")
            payment_method = "Google Pay"
            break


        elif payment_method == "apple pay":
            user_login(users.apple_pay,"Apple Pay")
            payment_method =  "Apple Pay"
            break

        elif payment_method == "paypal":
            user_login(users.paypal,"Paypal")
            payment_method =  "paypal"
            break
        else:
            print("not a valid payment method")



# now the flight destination will be chosen
    while True:
        destination = input("What city is your destination?  ").strip().lower()
        if destination in cities:
            destination = destination
            print(f"Your destination is {destination}")
            break
        else:
            print("not a valid city ")

#choosing seating class 
    seating_class = class_selection()
    seat_position = seat_selection(seating_class)

    adjusted_price = price(seating_class)

# loyalty program 
    saved = loyalty()
    bag_price = bag_check()
    adjusted_price = adjusted_price - saved + bag_price
    adjusted_price = adjusted_price * 1.13

    print(f"Your flight to {destination} has been placed.\n Your seat is {seat_position} \n The price of your flight is ${adjusted_price} \n Thank you for ordering with us!")
if __name__ == "__main__":
    main()






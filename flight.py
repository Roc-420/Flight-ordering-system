

from tabulate import tabulate
from emoji import emojize
import random
from colorama import Fore, Back, Style
from function import real_time_flight_info,seat_selection,class_selection,user_attentification,user_create
class users:    
    air_ontario = []
    paypal = []
    google_pay = []
    apple_pay = []
class current_users:
    air_ontario = []
    paypal = []
    google_pay = []
    apple_pay = [] 

import pickle


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


# thank you message and meaning of status symbols

    print("Thank you for choosing Air Ontario")
    print(emojize(" -:red_circle: means the flight is cancelled"))
    print(emojize(" -:green_circle: means the flight is on time"))    
    print(emojize(" -:yellow_circle: means the flight is delayed"))
    print(emojize(" -:blue_circle: means the flight has arrived"))

    # here it will let users check the additional info of a flight



    #here we will start letting the user do flight orders

    while True:
        _ = input("Would you like to purchase a flight?   ").strip().lower()

        if _  == "yes":
            break
    
        elif _ == "no":
            return None
    
        else:
            pass

# creates a new account if the user wants it 
    user_create(users.paypal,"Paypal")
    user_create(users.apple_pay,"Apple Pay")
    user_create(users.google_pay,"Google Pay")
    user_create(users.air_ontario, "Air Ontario")

# we create 

    


if __name__ == "__main__":
    main()
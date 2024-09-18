import random
from emoji import emojize
from tabulate import tabulate
from colorama import Fore, Back, Style
import csv

#due to the scale of this project, features will be made into function
def user_login(list_of_users,account):

    while True:
        user = input(f"Enter a userfor {account}:  ").lower().strip()
        password = input("Enter a password:  ").lower().strip()
        if match({"user":user,"password":password},list_of_users):
            print("correct login !")
            return {"user":user,"password":password}
    
        else:
            print("incorrent login !")

def match(dict,list): # checks to see if dict is in a list
    for dictionary in list:
        if dict == dictionary:
            return True
        else:
            pass
    return False # it will reach this if the return true statement does not occur
#since air ontario isnt a current company, flight,info will be randomly generated and flight times

def real_time_flight_info():
    status = random.randrange(0,4) # each number represents a status delayed,etc 
    status_time= [] # will contain status,departure time,arrival time

    """
    0 == cancelled
    1 == ontime
    2== arrived
    3: == delayed 
    """

    # creating status
    if status == 0:
        status_time.append (emojize(":red_circle:"))
    
    elif status == 1:
        status_time.append  (emojize(":green_circle:"))
    
    elif status == 2:
        status_time.append (emojize(":blue_circle:"))
    
    elif status == 3:
        status_time.append (emojize(":yellow_circle:"))

    if status == 0 or status == 2: # an arrived  or cancelled flight doe not have a flight time
        status_time.append ("----")
        status_time.append ("----")

    else: # generating flight time for ontime or delayed flights, 24 hour time will be used here, here it will be assumed the days of the flight are pre set and static and therefore will not change
        time = random.randrange(0,5)# fligt time is between 0 to 4 hours
        minutes_1 = random.randrange(0,60) # departure time minutes
        minutes_2 = random.randrange(0,60) # arrival time minutes 
        departure_time = random.randrange(0,25)# generated departure time

        if time + departure_time <= 24:
            arrival_time = time + departure_time

        else:
            arrival_time = (time + departure_time) - 24

        
        status_time.append(f"{departure_time}:{minutes_1}")
        status_time.append(f"{arrival_time}:{minutes_2}")

    return  status_time


def class_selection():
    while True:
        seat_class = input("What seating class would you like(business, economy or first class):  ").strip().lower()
        if seat_class == "business" or seat_class == "economy" or seat_class == "first class":
            return seat_class
        else:
            print("not valid seating class ")

def seat_selection(seat_class): # random generates a seat number and allows the user to choose one, seat availability is randomly generated 
    row_number = 4 # this will stay static while the column size will change depending on what class is chosen 

    if seat_class == "economy":
        column_number = 11

    elif seat_class == "business":
        column_number = 5

    elif seat_class == "first class":
        column_number = 3

        # now an array will be populated with the seats depending on the what class is chosen
    seat_arrangement_display = []
    seating_arrangement_available = []
    alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x','y' ,'z']


    for c in range(column_number): # for loop for generated columns
        row_display = [] # generates a new empty row 
        row_available = []
        for i in range(row_number):
            # randomly generates if a seat is available or not, two seperate arrays will be used, one for the seating plan and one for only the evailable seats
            availability = random.randrange(0,2)
            if availability == 1: # if it is avaialable
                row_available.append(f"{alphabet[c]}{i}")
                row_display.append(f"{Fore.GREEN}{alphabet[c]}{i}")
            else:
                row_display.append(f"{Fore.RED}{alphabet[c]}{i}")

        seat_arrangement_display.append(row_display)
        seating_arrangement_available.append(row_available)

    print(tabulate(seat_arrangement_display,tablefmt="double_grid"))

    print(Fore.RESET,"")
  
# finally  the user will be allowed to order a seat, verification will be done here as well.

    while True:
        final_seat = input("Enter what seat you would like:    ").strip().lower()

    #checking if item is in array 
        is_available = False
        for row in seating_arrangement_available:
            if final_seat in row:
                is_available = True

        if is_available == True:
            print(f"Your seat is {final_seat}.")
            return final_seat
        
        else:
            print("seat not available")



def length_check(info,minimum,maximum):
    if len(info) < minimum:
        print(f"{info} is too short")
        return False

    elif len(info) > maximum:
        print(f"{info} is too long")
        return  False

    else:
        print(f"{info} is valid.")
        return True

def user_create(user_dict,account_name):# will be used for creating a new user
    #allows user to opt out of creating an account if they would not like to 
    while True:
        desire = input(f"Would you like to create a user for {account_name}:  ").strip().lower()
        if desire == "yes":
            break
        elif desire == "no":
            return None



# user name and password will be checked to see if they are too long or too short first individualy
# than they will be checked to see if they already exist together
    while True:
        while True:
            username = input("Enter your new user name:   ").strip().lower()                  
            validity = length_check(username,4,30)

            if validity == True:

                break
            else:
                pass
        while True:
            password = input("Enter your new password :   ").strip().lower()                  
            validity = length_check(password,4,14)
            if validity == True:
                break
            else:
                pass


        if {"user":username,"password":password} in user_dict:
            print("username and password already exist!")


        else:
            print(f"An {account_name} account has been created with the username {username} ")
            user_dict.append({"user":username,"password":password})
            break
  

def data_storage(data_var,data_file): # will be used for merging a variable and a csv file together(only the unique terms) and writing it to the file
    data_dict = []
    field_names = ["user","password"]
    with open(data_file,'r') as file: # wdatill be acessing the dictionary here
        reader = csv.reader(file,delimiter=',')
        for row in reader:
            if row == []: # preventing error from occuring with blank line
                break
            else:
                new_item = {"user":row[0],"password":row[1]}
                data_dict.append(new_item)
        


    new_info = data_var # duplicated should be handled by the user create function

    with open(data_file,'a') as file:
        writer = csv.DictWriter(file,fieldnames = field_names)
        for row in new_info:
            writer.writerow(row)
# returns the complete list of data
    complete_data = data_dict + new_info
    return complete_data



    # for the loyalty program, everytime a purchase is made by a user, the amount of purchased made will be saved to a csv file, than a multiplier will be added to determine the number of flight
    # poiints which will then be used to determine the amount of saving a user infers

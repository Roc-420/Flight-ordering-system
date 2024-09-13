import random
from emoji import emojize



#due to the scale of this project, features will be made into function, getting inputs from a user will be given in the function parameters to make unit tests for it
#additionally the list of users and password will be taken as a paramter as well so it can be modified outside 
def user_attentification(user,password,list_of_users):

    if [user,password] in list_of_users:
        return True
    
    else:
        return False
    

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

        
        status_time.append(f"{departdure_time}:{minutes_1}")
        status_time.append(f"{arrival_time}:{minutes_2}")

    return status_time[0],status_time[1],status_time[2]


def class_selection():
    while True:
        seat_class = input("What seating class would you like(business, economy or first class):  ").strip().lower()
        if seat_class == "business" or seat_class == "economy" or seat_class == "first class":
            return seat_class
        else:
            print("not valid seat ")

def seat_selection(seat_class,): # random generates a seat number and allows the user to choose one, seat availability is randomly generated 
    row = 4 # this will stay static while the column size will change depending on what class is chosen 
    base_price = 200 #base flight price that will be modified depending on what class was chosen
    #chooses class 
    """
     economy is class = 9 columns
     bussiness class = 4 columns
     first class = 2 columns 
    """
    if seat_class == "economy":
        column = 9

    elif seat_class == "business":
        column = 4

    elif seat_class == "first class":
        column = 2

        # now an array will be populated with the seats depending on the what class is chosen


    


from tabulate import tabulate
from emoji import emojize
import random


def main():

    flight_info = ["City","Flight Number","Terminal","Status","Time of departure","Time of arrival"]
    regina = ["Regina","1265"," 01",]
    thunder_bay = ["Thunder Bay","1111","00"]
    winnipeg= ["Winnepeg"," 9000","02"]
    ottowa = ["Ottowa","1089"," 06"]
    yellow_knife=["Yellow Knife"," 1766","04"]
    pei = ["PEI","7894", "01"]
    halifax = ["Halifax"," 4444"," 03"]
    edmonton = ["Edmonton","5674"," 02"]
    hamilton = ["Hamilton"," 5555"," 00 "]
    montreal = ["Montreal","1234","04"]
    vancouver= ["Vancouver","4356","05"]
    calgary = ["Calgary", " 5567","00"]

    
#merging all the lists into an array 
    complete_list = [flight_info,regina,thunder_bay,winnipeg,ottowa,yellow_knife,pei,halifax,edmonton,hamilton,montreal,vancouver,calgary]
    print(tabulate(complete_list, tablefmt="modern"))


#due to the scale of this project, features will be made into function, getting inputs from a user will be given in the function parameters to make unit tests for it
def user_attentification(user,password):
    list_of_users= [["user1","1234"],["user2","4321"],["user3","0000"]]     #list of users user can log in as 

    if [user,password] in list_of_users:
        return True
    
    else:
        return False
    

#since air ontario isnt a current company, flight,info will be randomly generated and flight times

def real_time_flight_info():
    status = random.randrange(0,5) # each number represents a status delayed,etc 
    status_time= [] # will contain 

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

    if status == 0 or status == 2: # a delayed or cancelled flight doe not have a flight time
        status_time.append ("----")

    else: # generating flight time for ontime or delayed flights
        time = random.randrange(0,5)# fligt time is between 0 to 4 hours
        








if __name__ == "__main__":
    main()
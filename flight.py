

from tabulate import tabulate
from emoji import emojize
import random

def main():

    flight_info = ["City","Flight Number","Terminal","Status","Time of departure","Time of arrival"]
    regina = ["Regina","1265"," 01",real_time_flight_info(),"12:00 AM","2:00 PM"]
    thunder_bay = ["Thunder Bay","1111","00",emojize(":green_circle:"),"7:00AM", "1:30PM"]
    winnipeg= ["Winnepeg"," 9000","02",emojize(":yellow_circle:"),"5:57PM" ,"9:44PM"]
    ottowa = ["Ottowa","1089"," 06",emojize(":red_circle:")," ----- "," -----  "]
    yellow_knife=["Yellow Knife"," 1766","04",emojize(":yellow_circle:"),"2:24 PM", "7:44 PM"]
    pei = ["PEI","7894", "01",emojize(":green_circle:"),"11:00PM", "3:56AM" ]
    halifax = ["Halifax"," 4444"," 03",emojize(":green_circle:"),"4:30 PM","12:14AM"]
    edmonton = ["Edmonton","5674"," 02",emojize(":yellow_circle:")," 4:14PM"," 7:46PM"]
    hamilton = ["Hamilton"," 5555"," 00 ",emojize(":red_circle:") ," -----", " -----"]
    montreal = ["Montreal","1234","04",emojize(":green_circle:"),"12:40PM"," 3:39PM"]
    vancouver= ["Vancouver","4356","05",emojize(":green_circle:"),"5:14AM","7:34PM"]
    calgary = ["Calgary", " 5567","00",emojize(":red_circle:")," ----",  " ----"]

    
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
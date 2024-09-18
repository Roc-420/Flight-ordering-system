

from function import seat_selection
from function import user_create
from function import user_login
from colorama import Fore, Back, Style
from tabulate import tabulate
from function import data_storage

import csv
paypal = [ {"user":"user_9","password":"password_9"},{"user":"user_10","password":"password_10"},{"user":"user_11","password":"password_11"} ]
print(paypal)
#data_storage(paypal,'test.csv')
ls= user_create(paypal,"paypal")
print(paypal)
user_login(paypal)
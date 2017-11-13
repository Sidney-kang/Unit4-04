# Created by : Sidney Kang
# Created on : 29 Oct. 2017
# Created for : ICS3UR
# Daily Assignment - Unit4-04
# This program converts a level into a percentage and returns the middle 
#   percentage mark

percentage_4_plus = 98
percentage_4 = 91
percentage_4_minus = 83
percentage_3_plus = 78
percentage_3 = 75
percentage_3_minus = 71
percentage_2_plus = 68
percentage_2 = 65
percentage_2_minus = 61
percentage_1_plus = 58
percentage_1 = 55
percentage_1_minus = 51
percentage_NE = 25

def calculate_average(user_input):
	     
     if user_input == "NE":
        user_input = percentage_NE
        print("You mark in percentage is: " + str(user_input) + "%")
     elif user_input == "1+":
        user_input = percentage_1_plus
        print("You mark in percentage is: " + str(user_input) + "%")
     elif user_input == "1":
        user_input = percentage_1
        print("You mark in percentage is: " + str(user_input) + "%")
     elif user_input == "1-":
        user_input = percentage_1_minus
        print("You mark in percentage is: " + str(user_input) + "%")
     elif user_input == "2":
        user_input = percentage_2
        print("You mark in percentage is: " + str(user_input) + "%")
     elif user_input == "2+": 
        user_input = percentage_2_plus
        print("You mark in percentage is: " + str(user_input) + "%")
     elif user_input == "2-": 
        user_input = percentage_2_minus
        print("You mark in percentage is: " + str(user_input) + "%")    	
     elif user_input == "3":
        user_input = percentage_3
        print("You mark in percentage is: " + str(user_input) + "%")
     elif user_input == "3+":
        user_input = percentage_3_plus
        print("You mark in percentage is: " + str(user_input) + "%")
     elif user_input == "3-":
        user_input = percentage_3_minus
        print("You mark in percentage is: " + str(user_input) + "%")
     elif user_input == "4":
        user_input = percentage_4
        print("You mark in percentage is: " + str(user_input) + "%")
     elif user_input == "4+":
        user_input = percentage_4_plus
        print("You mark in percentage is: " + str(user_input) + "%")
     elif user_input == "4-":
        user_input = percentage_4_minus
        print("You mark in percentage is: " + str(user_input) + "%")
     else:
        print("-1")
        ask_mark()
        
def ask_mark(): 	  
    user_input = raw_input("Please enter any level from NE - 4+: ")    
    if user_input == "ne":
       user_input = user_input.upper()
        	       
    calculate_average(user_input)   	

ask_mark()        

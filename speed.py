

from time import *
import random as r 

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except IndexError:  # Specifically catch IndexError
            error += 1
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s  # Calculate the time difference
    time_R = round(time_delay, 2)  # Round the time taken
    speed = len(userinput) / time_R if time_R > 0 else 0  # Prevent division by zero
    return round(speed)

while True:
    ck = input("Ready to test: yes/no: ").strip().lower()  # Normalize input
    if ck == "yes":
        test = [
            "A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea.",
            "My name is Essa Khan.",
            "Welcome to WSCube Teach Jodhpur."
        ]

        test1 = r.choice(test)
        print("*****typing speed*****")
        print(test1)
        print()
        
        time_1 = time()
        testinput = input("Enter: ")
        time_2 = time()

        print('Speed:', speed_time(time_1, time_2, testinput), "w/sec")
        print("Error:", mistake(test1, testinput))
        
    elif ck == 'no':
        print("Thank you")
        break
    else:
        print("Invalid input, please enter 'yes' or 'no'.")

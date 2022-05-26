#!/usr/bin/env python
# coding: utf-8

# In[53]:


# celsius to Fahreinheat conversion

def celsius_to_fahreinheat():
    celsius_value = input("Please enter the celsius value to be converted ")   # user celsius input
    loopAgain = True
    
    while loopAgain:
        # checking for valid inputs and the nature of input if its int or float or string
        try:                                                                
            celsius_value = int(celsius_value)
            
            # Conversion formula
            
            fahreinheat_value = (9/5*celsius_value) + 32
            fahreinheat_value = round(fahreinheat_value, 2)
            print(f"The fahreinheat equivalent is {fahreinheat_value}")
            loopAgain = False

        except ValueError:
            try:
                celsius_value = float(celsius_value)
                fahreinheat_value = (9/5)*(celsius_value) + 32
                fahreinheat_value = round(fahreinheat_value, 2)
                print(f"The fahreinheat equivalent is {fahreinheat_value}")
                loopAgain = False
            # If we encounter string as input
            except ValueError:
                celsius_value = input("It's a string, please enter a valid number ")
                loopAgain = True
# Fahreinheat to celsius conversion

def fahreinheat_to_celsius():
    fahreinheat_value = input("Please enter the fahreinheat value to be converted ")
    loopAgain = True
    
    while loopAgain:
        # Checking for the nature of inputs if it is string or float or int
        
        try:
            fahreinheat_value = int(fahreinheat_value)
            
            # Conversion formula
            
            celsius_value = (5/9)*(fahreinheat_value - 32)
            celsius_value = round(celsius_value, 2)
            print(f"The celsius equivalent is {celsius_value}")
            loopAgain = False

        except ValueError:
            try:
                fahreinheat_value = float(fahreinheat_value)
                celsius_value = (5/9)*(fahreinheat_value - 32)
                celsius_value = round(celsius_value, 2)
                print(f"The celsius equivalent is {celsius_value}")
                loopAgain = False
                

            except ValueError:
                fahreinheat_value = input("Not a number, please enter a number ")
                loopAgain = True

# Getting the input from user               

user_input = input("please choose (A) C_to_F  or (B) F_to_C ").lower()

# Checking for the inputs
loop_more = True
while loop_more:
    if user_input == 'a':
        celsius_to_fahreinheat()
        loop_more = False
    elif user_input == 'b':
        fahreinheat_to_celsius()
        loop_more = False
    else:
        user_input =input("Enter a valid choice")
        loop_more = True




    


# In[ ]:





# In[ ]:





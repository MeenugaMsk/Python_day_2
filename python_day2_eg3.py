#!/usr/bin/env python
# coding: utf-8

# In[34]:


# Sorting
# defining low to high and high to low functions

def low_to_high():
    list.sort()
    print(list)

def high_to_low():
    list.sort(reverse = True)
    print(list)
# creating an empty list

list = []
# getting 5 values as input from the user

for index in range(5):
    go = True
    # validating for the correct inputs
    
    while go:
        num = input("enter the value ")
        try:
            num = int(num)
            list += [num]
            go = False
        except ValueError:
            try:
                num = float(num)
                list += [num]
                go = False
            except ValueError:
                print("Not a valid number ")
                go = True
# Displaying the numbers given by user
print(f"List of numbers given by you are {list}")

# Asking for user choice and checking its validity
loopAgain = True                

while loopAgain:
    
    choice = input("(a). low_to_high (b). high_to_low ").lower()


    if choice == 'a':
        low_to_high()
        loopAgain = False
    elif choice == 'b':
        high_to_low()
        loopAgain = False
    else:
        print("Enter a valid input")
        loopAgain = True


# In[ ]:





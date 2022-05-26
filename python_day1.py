#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[26]:


#taking number from user
n = input("enter the number")
loopAgain = 1
# checking whether to loop again or not
while loopAgain ==1:
    # checking if the number is valid or not
    if(n.isdigit()):
        a = int(n)
        # checking if the number is odd or even
        if (a%2 == 0):
            print("Even number")
        else:
            print("odd number")
        loopAgain = 0
    else:
        n = input("enter a valid number")
        loopAgain = 1


# In[36]:


#taking number from user
n = input("enter the number")
loopAgain = 1
# checking whether to loop again or not
while loopAgain ==1:
    # checking if the number is valid or not
    if(n.isdigit()):
        a = int(n)
        sum = 0
        #calculating the sum
        for var in range(1, a+1):
            sum = sum + var
        print(f"The sum is {sum}")
        loopAgain = 0
    else:
        n = input("enter a valid number")
        loopAgain = 1


# In[65]:


# Getting input from the user

n = input("enter the number")

# Checking if the number is valid or not

loopAgain = 1 

while loopAgain == 1:
    
    if(n.isdigit()):
        n = int(n)
        sum = 0
        temp = n
        
        # Checking for Armstrong property
        
        while n > 0:
            r = n % 10
            c = (r*r*r)
            sum = sum + c
            n = int(n/10)
        print(sum)
        n = temp
        # displaying the result
        
        if (sum == n):
            print("Armstrong number")
        else:
            print("Not an Armstrong number")
        loopAgain = 0    
    else:
        n = input("Please enter a valid number")
        loopAgain == 1
        


# In[23]:


# Printing the next Armstrong number
loopAgain = True
while loopAgain:
    previous = input("enter the present Armstrong number")
    if(previous.isdigit()):
        previous = int(previous)
        is_Armstrong = False
        present = (previous) + 1
        while not is_Armstrong:
            present = previous + 1
            sum = 0
            temp = present
            while (present > 0):
                r = present % 10
                c = (r*r*r)
                sum = sum + c
                present = int(present/10)
            present = temp
            if (present == sum):
                print(f"Next Armstrong number is {present}")
                is_Armstrong = True
            else:
                previous = present 
                is_Armstring = False
        loopAgain = False
    else:
        print("Please enter a valid number")
        loopAgain = True


        
    
    


# In[25]:


# DEFINING FUNCTIONS SEPARATELY FOR THE AVAILABLE OPTIONS

def sum_of_numbers():
    #taking number from user
    n = input("enter the number")
    loopAgain = 1
    # checking whether to loop again or not
    while loopAgain ==1:
        # checking if the number is valid or not
        if(n.isdigit()):
            a = int(n)
            sum = 0
            #calculating the sum
            for var in range(1, a+1):
                sum = sum + var
            print(f"The sum is {sum}")
            loopAgain = 0
        else:
            n = input("enter a valid number")
            loopAgain = 1
def odd_or_even():
    #taking number from user
    n = input("enter the number")
    loopAgain = 1
    # checking whether to loop again or not
    while loopAgain ==1:
        # checking if the number is valid or not
        if(n.isdigit()):
            a = int(n)
            # checking if the number is odd or even
            if (a%2 == 0):
                print("Even number")
            else:
                print("odd number")
            loopAgain = 0
        else:
            n = input("enter a valid number")
            loopAgain = 1
def Armstrong_Number():
    # Getting input from the user

    n = input("enter the number")

    # Checking if the number is valid or not

    loopAgain = 1 

    while loopAgain == 1:

        if(n.isdigit()):
            n = int(n)
            sum = 0
            temp = n

            # Checking for Armstrong property

            while n > 0:
                r = n % 10
                c = (r*r*r)
                sum = sum + c
                n = int(n/10)
            print(sum)
            n = temp
            # displaying the result

            if (sum == n):
                print("Armstrong number")
            else:
                print("Not an Armstrong number")
            loopAgain = 0    
        else:
            n = input("Please enter a valid number")
            loopAgain == 1

# MAIN PROGRAM
    
print("A. Sum of numbers B. Odd or Even number C.Armstrong Number D.Exit")
user_input = input("Choose an option ").lower()
correct_input = 1

# CHECKING FOR THE VALIDITY OF INPUT

while correct_input == 1:
    if user_input == 'a':
        sum_of_numbers()
        correct_input = 0
    elif user_input == 'b':
        odd_or_even()
        correct_input = 0
    elif user_input == 'c':
        Armstrong_Number()
        correct_input = 0
    elif user_input == 'd':
        print("Bye !")
        correct_input = 0
    else:
        user_input = input("Please enter a valid input ")
        correct_input = 1     

    
    
    

    


# In[ ]:





# In[ ]:





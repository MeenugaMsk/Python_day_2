#!/usr/bin/env python
# coding: utf-8

# In[35]:


# Fibonacci sequence generator

# defining function for fibonacci numbers generation

def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            print(c)
            a = b
            b = c

# Getting input from the user            

n = input("Please enter the number of digits to be generated ")
loopAgain = True

# checking for the validity of input
while loopAgain:
    if (n.isdigit()):
        n = int(n)
        fib(n)
        loopAgain = False
    else:
        n = input("Please enter a valid number ")
        loopAgain = True


# In[ ]:





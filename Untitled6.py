#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a Python function to sum all the numbers in a list
a = [8, 2, 3, 0, 7]
added = 0
for i in range(len(a)):
    added+=a[i]
print(added)


# In[6]:


#Write a Python program to reverse a string
my_str = input("Please enter your own String : ")
str = ''
for i in my_str:
    str = i + str
print("\nThe Original String is: ", my_str)
print("The Reversed String is: ", str)


# In[9]:


#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
            pass
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brow Fox')


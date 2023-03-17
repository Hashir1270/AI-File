#!/usr/bin/env python
# coding: utf-8

# # Help Function

# In[1]:


name = "Muhammad Hashir"

print(name)
print(len(name)) # length of variable
print(type(name)) # variable type
print(id(name)) # memory address of variable 
print(dir(name)) # all method and attributes of variable


# In[2]:


age = "21"

print(age)
print(len(age)) # length of variable
print(type(age)) # variable type
print(id(age)) # memory address of variable 
print(dir(age)) # all method and attributes of variable


#  # Text formating/formation/concatinaation

# In[3]:


first name = "Muhammad Hashir"


# # Rule for Python variables:
# * A variable name must start with a letter or the underscore character
# * A variable name cannot start with a number
# * A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# * Variable names are case-sensitive (age, Age and AGE are three different variables)
#  *A variable name cannot be any of the Python keywords.

# In[4]:


student_name = "Muhammad Hashir"
print(student_name)


# In[5]:


a = len("Muhammad Hashir") # return function 
print(a)
print(a)
print(a)


# In[6]:


a = print("Muhammad Hashir") # return function 
print(a)
print(a)
print(a)


# In[9]:


a = print("""
sylani Mass IT program
Batch-4 AI and DS
Class days: Tues and Fri
""")
print(a)
print(a)
print(a)


# # Concationation
# * +
# * variable_name.format (var1,var2,var3)
# * 'f' 'student name: {var1}'

# In[21]:


first_name= "Muhammad"
last_name = "Hashir"
institude_name = "Sylani Mass IT Training"
age = "21"
card = "Institude_name: " + institude_name + "\nstudent Full Name: " + first_name+ " " + last_name+ "\nAge: " +age
print(card)


# In[11]:


age = 21
print(age, type(age))

# type casting 
age = 21


# In[26]:


first_name= "Muhammad"
last_name = "Hashir"
institude_name = "Sylani Mass IT Training"
age = "21"


card = """Institude Name: {}
Student Full Name: {}{}
Age: {} """.format (institude_name,forst _name,last_name,age)
#              0              1           3
print(card)


# # with f

# In[28]:


first_name= "Muhammad"
last_name = "Hashir"
institude_name = "Sylani Mass IT Training"
age = 21


card = F"""Institude Name: {institude_name}
Student Full Name: {first_name}{last_name}
Age: {age} 
"""
print(card)


# In[31]:


card = """Institude Name: %s
Student Full Name: %s %s 
Age: %d
""" % (institude_name, first_name, last_name,age)
print(card)


# In[44]:


for idx, i in enumerate([i for in dir(card) if "_" not in i]):
    print(idx,i)


# In[40]:


print (card.capitalize())


# In[41]:


print(card.casefold()) # inline 


# In[42]:


print(card)


# In[56]:


print(card)
card.count('Hashir')


# In[57]:


print(card)
card.casefold().count('Hashir')


# In[58]:


txt = "My name is Ståle"

x = txt.encode()

print(x)


# In[59]:


txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))


# In[ ]:





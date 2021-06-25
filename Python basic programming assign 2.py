#!/usr/bin/env python
# coding: utf-8

# ## Coverting kilometers to miles

# In[12]:


km = float(input("Enter value in kilometers: "))
miles = 0.621371*km
print(km,"km is: ",miles,"Miles")


# ## Converting Celsius to Fahrenheit

# In[14]:


Celsius= float(input("Enter value in celcius: "))
Fahrenheit = (Celsius * 9/5) + 32
print(Celsius,"Celsius is: ",Fahrenheit,"Fahrenheit")


# ## Display calendar

# In[13]:


import calendar
#if we write tuesday the calendar will start with tuesday 
c= calendar.TextCalendar(calendar.SUNDAY)
calendar = c.formatmonth(int(input("Enter the year: ")),int(input("Enter the month number: ")))
print(calendar)


# ## Solve quadratic equation

# In[8]:


a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))
c = int(input("Enter a number c: "))
solution1 = ((-b +(b ** 2 - 4 * a * c) ** 0.5) / 2 * a)
solution2 = ((-b -(b ** 2 - 4 * a * c) ** 0.5) / 2 * a)
print("Solutions of the quadratic equation are {} and {}".format(solution1,solution2))


# ## Swapping

# In[11]:


a=input("Enter a number a: ")
b=input("Enter anaother number b: ")
b,a=a,b
print("Swapped a: ",a)
print("Swapped b: ",b)


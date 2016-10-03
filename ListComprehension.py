
# coding: utf-8

# In[4]:

l = []


# In[5]:

for i in "Word":
    l.append(i)
print l


# In[7]:

l2 = [x**2 for x in range(0,100,5) ]
print l2


# Q. Find even Numbers using list Comprehension. Use range upto 100

# In[10]:

L3 = [number for number in range(0,100) if number%2==0]
print L3


# Q. Convert Celsius to Fahrenheit

# In[13]:

Celsius = [10,20,56, 35.6,32,0]

Fahrenheit = [c*(9/5)+32 for c in Celsius]

print Fahrenheit


# In[ ]:




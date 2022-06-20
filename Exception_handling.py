#!/usr/bin/env python
# coding: utf-8

# In[15]:


a = 10
b= 20
c = a+'s'
print(c)


# In[12]:


# compile time error(systax error) and run time error(exception error).


# In[16]:


# sorce code --> compile code --> byte code --> interpritor


# In[20]:


a = int(input("enter the first number"))
b =int(input("enter the second number"))
c = a/b
print(c)
d = a*b
print(d)


# In[23]:


# try:
# except:
# else:
# raise:
# finally:


# In[26]:


a = int(input("enter the first number"))
b =int(input("enter the second number"))
try:
    c = a/b
    print(c)
except ZeroDivisionError:
    pass
d = a*b
print(d)


# In[29]:


a = int(input("enter the first number"))
b =int(input("enter the second number"))
try:
    c = a/b
    print(c)
except SyntaxError:
    pass
d = a*b
print(d)


# In[39]:


a = int(input("enter the first number"))
b =input("enter the second number")
try:
    c = a/b
    print(c)
except ZeroDivisionError:
    pass
except ValueError:
    pass

    #print("b should not be a zero")


# In[40]:


format 


# In[ ]:





# In[ ]:





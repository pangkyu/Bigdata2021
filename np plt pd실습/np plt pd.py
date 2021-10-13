#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


x = [1,6,7]
y = [20,30,50]


# In[3]:


plt.plot(x, y)


# In[6]:


x = np.linspace(0, 10, 100) # 0부터 10까지 데이터 100개로 일정하게 쪼갬


# In[7]:


x


# In[8]:


plt.plot(x,np.sin(x))


# In[10]:


ax = plt.axes()
ax.plot(x, np.sin(x))


# In[18]:


plt.plot(x,np.sin(x), color = 'red', linestyle = 'solid' , label = 'sin(x)')
plt.plot(x,np.cos(x), color = 'g', linestyle = '--', label = 'cos(x)')
plt.title( 'sin & cos curves')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.ylim((-1.2, 1.2))
plt.legend()


# In[20]:


x


# In[21]:


y


# In[25]:


np.random.seed(1)
dat = np.random.random(1000)


# In[26]:


plt.hist(dat)


# In[27]:


np.random.seed(2)
x1 = np.random.normal(0,0.8, 1000)
x2 = np.random.normal(-2,1,1000)


# In[28]:


plt.hist(x1)
plt.hist(x2)


# In[29]:


plt.hist(x1, alpha = 0.5, bins = 30)
plt.hist(x2, alpha = 0.5, bins = 30)


# In[30]:


plt.subplot(2,3,1)
plt.plot(np.random.random(10))
plt.subplot(2,3,2)
plt.plot(np.random.random(10))
plt.subplot(2,3,6)
plt.plot(np.random.random(10))


# In[ ]:





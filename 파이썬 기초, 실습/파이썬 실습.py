#!/usr/bin/env python
# coding: utf-8

# In[17]:


import math
class Circle:
    def __init__(self, r):
        self.radius = r
    def get_radius(self):
        return self.radius
    def getArea(self):
        return math.pi * self.radius ** 2 
    def __le__(self, other):
        return self.radius <= other.radius


# In[18]:


my_circle = Circle(5)


# In[19]:


my_circle.get_radius()


# In[20]:


my_circle.getArea()


# In[21]:


c1 = Circle(5.2) 
c2 = Circle(2.0)
c1 <= c2


# In[22]:


c2 <= c1


# In[23]:


import numpy as np


# In[28]:


a = np.array([1,2,3])


# In[32]:


type(a)


# In[33]:


a.ndim


# In[34]:


a.dtype


# In[1]:


import numpy as np
a = np.array([4,2,6])
type(a)


# In[2]:


print(a)


# In[3]:


a


# In[4]:


a.ndim


# In[5]:


a.shape


# In[6]:


a.dtype


# In[7]:


b = np.array([[1,2,3], [4,5,6]])


# In[8]:


b.ndim


# In[9]:


b


# In[10]:


b.shape


# In[11]:


zp,zeros(10)


# In[12]:


np.zeros(10)


# In[13]:


np.full((3,4), 3)


# In[14]:


np.arange(100)


# In[15]:


np.linspace(0,10,3)


# In[16]:


np.linspace(0,10,4)


# In[17]:


np.random.random()


# In[18]:


np.random.seed(1)


# In[19]:


np.random.random((3,4))


# In[20]:


np.random.seed(0)


# In[21]:


np.random.random((3,4))


# In[22]:


np.random.normal


# In[23]:


np.random.randint(0, 10, (3,4))


# In[24]:


np.random.normal(0,1,(3,4))


# In[25]:


a = np.arange(5, 15, 2)
b = np.random.randint(1,11, size = (2,5))


# In[26]:


a
b


# In[27]:


a


# In[28]:


b


# In[30]:


a[1:4]


# In[31]:


b[1, 1:]


# In[32]:


b[1, 1:4]


# In[33]:


b[1, 1:5]


# In[34]:


b[1:2, 1:5]


# In[35]:


b[1]


# In[36]:


b[1, :]


# In[37]:


b[:, 2]


# In[38]:


b2 = b[:,2]


# In[39]:


b2


# In[40]:


grid  = np.arange(1,10).reshape((3,3))


# In[41]:


grid


# In[44]:


a = np.array([2,4,8]).reshape((3,1))


# In[45]:


a.shape


# In[46]:


a.ndim


# In[47]:


m = np.arange(1,11).reshape(2,5)


# In[48]:


m


# In[49]:


m.transpose()


# In[50]:


m.T()


# In[52]:


r = np.arange(1,20,3)


# In[53]:


r


# In[59]:


a, b, c = np.split(r, [2,5])


# In[60]:


a


# In[61]:


b


# In[ ]:





# In[62]:


c


# In[ ]:





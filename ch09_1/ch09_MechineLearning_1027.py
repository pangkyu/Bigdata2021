#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 


# In[2]:


X = np.arange(10).reshape(10,1)


# In[3]:


y = np.array([-1,2,3,5,4,7,6,6,9,9])


# In[4]:


X.shape #2차원


# In[5]:


y.shape #1차원


# In[6]:


plt.scatter(X,y)


# In[7]:


from sklearn.linear_model import LinearRegression


# In[8]:


reg = LinearRegression()


# In[9]:


type(reg)


# In[10]:


reg.fit(X,y)


# In[11]:


reg.coef_


# In[12]:


reg.intercept_


# In[13]:


# y = 0.64 + 0.96*x


# In[14]:


pred = reg.predict(X)


# In[15]:


pred


# In[17]:


plt.scatter(X,y)
plt.plot(X, pred , c = 'r')


# In[18]:


reg2 = LinearRegression(fit_intercept=False)


# In[19]:


reg2.fit(X,y)


# In[20]:


reg2.coef_


# In[21]:


reg2.intercept_


# In[24]:


pred2 = reg2.predict(X)


# In[25]:


pred2


# In[26]:


plt.scatter(X,y)
plt.plot(X, pred,  c = 'r')
plt.plot(X, pred2, c = 'g')


# In[28]:


reg.score(X,y) # 결정계수(R^2) ==> 1에 가까울수록 더 좋은값


# In[29]:


reg2.score(X,y)


# In[ ]:





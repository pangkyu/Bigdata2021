#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
df = pd.read_csv(path, header=None)
df.columns =  ['sepal length', 'sepal width', 'petal length', 'petal width', 'species'] 
X = df.drop('species', axis=1).to_numpy()
y = df['species'].to_numpy()
y = np.where(y == 'Iris-setosa', 0, np.where(y == 'Iris-versicolor', 1, 2))


# In[5]:


X = X[:, [2,3] ]


# In[6]:


X.shape


# ## 데이터 분할(훈련용 VS 테스트용)

# In[9]:


from sklearn.model_selection import train_test_split


# In[18]:


X_train, X_test, y_train, y_test = train_test_split(X,y, train_size = 0.7, random_state = 1, stratify = y)
#train_size, test_size => 훈련, 테스트 사이즈를 정할 수 있다.
# random_state => 
# stratify => 


# In[19]:


X_train.shape


# In[20]:


y_train.shape


# In[21]:


pd.Series(y_train).value_counts()


# In[22]:


pd.Series(y_test).value_counts()


# - x축 : 꽃잎의 길이(0번째 칼럼) 
# - y축 : 꽃잎의 너비(1번째 칼럼)
# - 품종별로 다른 색깔로 표시하기 

# In[27]:


ax = plt.axes()
markers = [ 's', 'x', 'o' ]
colors = [ 'r', 'g', 'b']
labels = ['setosa', 'versicolor', 'virginica']
for i in range(3):
    X_sub = X_train[y_train == i] #품종이 i 인거만 뽑힘 
    ax.scatter(X_sub[:, 0] , X_sub [:, 1], marker = markers[i], c = colors[i], label = labels[i], alpha = 0.5)
    ax.set(xlabel = 'Petal Length', ylabel = 'Petal Width')
    ax.legend()


# In[28]:


from sklearn.preprocessing import StandardScaler


# In[29]:


sc = StandardScaler()


# In[31]:


sc.fit(X_train)


# In[33]:


X_train_std  = sc.transform(X_train)


# In[35]:


X_test_std = sc.transform(X_test)


# In[36]:


X_train_std


# In[37]:


X_train


# ## 로지스틱 회귀

# In[38]:


from sklearn.linear_model import LogisticRegression


# In[39]:


logistic = LogisticRegression()


# In[41]:


logistic.fit(X_train_std, y_train)


# In[42]:


logistic.predict(X_train_std[:3, :])


# In[53]:


logistic.predict_proba(X_train_std[:3, :]) # 0일 확률 | 1일확률 | 2일 확률


# In[44]:


y_train[:3]


# In[45]:


logistic.score(X_train_std, y_train) # 정확도(accuracy)


# In[47]:


logistic.score(X_test_std, y_test) # test값에서 잘 나오는 것이 중요! 


# In[49]:


# 정오분류표 만들기 


# In[50]:


from sklearn.metrics import confusion_matrix


# In[51]:


y_pred = logistic.predict(X_test_std) # test data에 대한 예측 분류값
confusion_matrix(y_test, y_pred)


# In[ ]:





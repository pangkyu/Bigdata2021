#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# # 누락된 데이터 처리

# In[3]:


a = np.array([4,2, np.nan, 5])


# In[5]:


a.dtype # np.nan이 float이기 때문에 float형


# In[6]:


np.sum(a) # np.nan때문에 값은 nan이 나온다. 


# In[7]:


np.nansum(a)


# In[8]:


df = pd.DataFrame([[1,2,],[3,np.nan]], columns = ['x', 'y']) # 2차원 리스트 형태 


# In[9]:


df


# In[10]:


df.isnull()


# In[11]:


df.notnull()


# In[13]:


df.dropna() # NaN값이 있는 모든 행을 삭제


# In[14]:


df.dropna(axis = 1) # Nan값이 있는 모든 열을 삭제 


# In[15]:


df.fillna(0) # Nan이 들어있는 셀을 0으로 변환


# # 타이타닉 데이터 분석

# In[16]:


titanic = pd.read_csv('titanic.csv')


# In[17]:


titanic


# In[19]:


titanic.info() # 결손이 있는 정보 : age, cabin, embarked. cabin : 방 호실


# In[22]:


titanic.describe() # 수치형 컬럼에 대한 요약 통계량


# In[26]:


titanic.Survived.unique() # Survived에 있는 유니크한 값. -> 0,1 두가지 종류


# In[28]:


titanic.Name.unique().shape # Name에 있는 유니크한 값의 갯수를 아는 방법. ==> 891명의 승객이 이름이 전부 다르다. 


# In[29]:


titanic['Embarked'].unique()


# In[31]:


titanic['Embarked'].value_counts() # Embarked ==> 출항 항구 


# In[33]:


titanic.Cabin.isnull().sum() # true의 갯수를 센다.


# In[35]:


titanic.dropna().shape # 결손값이 들어있는 행들을 삭제 ==> 근데 너무 많이 데이터가 없어질 수 있다. (891 ==> 183)


# In[36]:


titanic2 = titanic.drop(['Cabin'], axis = 1) # Cabin열을 삭제하는 것이기때문에 axis = 1 을 꼭 넣어야함


# In[38]:


titanic2.shape


# In[39]:


titanic3 = titanic2.dropna() 


# In[40]:


titanic3.info()


# # 데이터 결합

# In[45]:


df1 = pd.DataFrame({'A': [1,2,3], 'B' : [4,5,6]}) # 딕셔너리. key-value


# In[46]:


df1


# In[47]:


df2 = pd.DataFrame({'A' : [10,20], 'B' : [40,45]}, index = [5,9])


# In[48]:


df2


# In[49]:


pd.concat([df1, df2]) # 리스트로 묶음


# In[50]:


df3 = pd.DataFrame({'C' : [5,2,8], 'D' : [10,50,-2]})


# In[51]:


df3


# In[52]:


pd.concat([df1, df3], axis = 1)


# In[53]:


df4 = df3.loc[0:1, :]


# In[54]:


df4


# In[58]:


pd.concat([df1, df4], axis = 1) # 일종의 외부조인(합집합) ==> join = 'outer'


# In[59]:


pd.concat([df1, df4], axis = 1, join = 'inner')#내부조인(교집합) 


# In[60]:


dept = pd.DataFrame({'name' : ['강', '박', '이', '최'], 'dep' : ['컴공', '컴공', '통계', '소융']})


# In[61]:


dept


# In[62]:


year = pd.DataFrame({'name' : ['이', '최', '강'], 'yr' : [2018,2016,2017]})


# In[63]:


year


# In[66]:


pd.merge(dept, year) # inner 가 디폴트옵션이다. (on = 'name' 생략해도 출력됨)


# In[67]:


pd.merge(dept, year, how = 'outer') # 외부조인으로 결과 출력


# In[68]:


year2 = pd.DataFrame({'student' : ['이', '최', '강'], 'yr' : [2018,2016,2017]})


# In[74]:


# pd.merge(dept, year2) ==> merge 에러가 발생한다. (조인을 하려는 공통 칼럼이 없기 때문에 ) 아래와 같이 작성
pd.merge(dept, year2, left_on = 'name', right_on = 'student')


# In[75]:


pd.merge(dept, year2, left_on = 'name', right_on = 'student'). drop('student', axis = 1) # name과 student가 같은 것을 나타내기때문에 생략


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # python keyword

# In[2]:


import keyword


# In[3]:


keyword.kwlist


# In[6]:


keyword.iskeyword('True')


# # 조건문

# In[8]:


size = 'M'
if size == 'S':
    length, width = 68.0, 52.0
elif size == 'M':
    length, width = 70.0, 54.5
else:
    length, width = 72.0, 57.0
print(length, width)


# In[9]:


get_ipython().run_line_magic('whos', '')


# In[10]:


get_ipython().run_line_magic('xdel', 'size')


# In[11]:


get_ipython().run_line_magic('whos', '')


# In[12]:


print(size)


# In[13]:


get_ipython().run_line_magic('reset', '')


# In[14]:


get_ipython().run_line_magic('whos', '')


# In[18]:


get_ipython().run_cell_magic('writefile', 'tsize.py', "if __name__ == '__main__':\n    size = 'L'\n    if size == 'S':\n        length, width = 68.0, 52.0\n    elif size == 'M':\n        length, width = 70.0, 54.5\n    else:\n        length, width = 72.0, 57.0\n    print(length, width)")


# In[19]:


get_ipython().run_line_magic('run', 'tsize.py')


# # 반복문

# In[20]:


n = 997
i = 2
while i < n:
    if n % i == 0:
        break
    i = i + 1
if i == n: # 2~ (n-1)로 나누어 떨어지는 i가 없다 
    print('소수')
else:
    print('소수가 아님')


# In[21]:


my_list = [4,2,5,7,3] # list
for x in my_list:
    print(x*2)


# In[25]:


for x in range(1, 10, 3):
    print(x, end = ' ')


# In[27]:


for _ in range(5):
    print('hello')


# In[28]:


def square(x):
    return x * x


# In[30]:


square(3)


# In[31]:


def abs(x):
    if x < 0:
        return -x
    else:
        return x


# In[32]:


abs(-5)


# In[33]:


def min_max(a, b):
    if a < b:
        return a, b
    else:
        return b, a


# In[34]:


min_max(8,3)


# In[46]:


def sum_to_n(n):
    """
    n까지의 자연수의 합을 반환하는 함수
    n이 정수가 아니면 TypeError발생
    n이 음수면 ValueError 발생
    """
    if type(n) is not int:
        raise TypeError('n은 정수형이어야 합니다.')
    if n < 0:
        raise ValueError('n은 0보다 커야합니다')
    sum = 0
    for i in range(n+1):
        sum += i
    return sum


# In[36]:


sum_to_n(9)


# In[47]:


get_ipython().run_line_magic('pinfo2', 'sum_to_n')


# In[45]:


sum_to_n(5.5)


# In[55]:


def sum_f(a, f):
    sum = 0
    for v in a:
        sum += f(v)
    return sum


# In[49]:



sum_f(my_list)


# In[53]:


def sq(x): return x * x


# In[56]:


my_list = [5,2,4]
sum_f(my_list, sq)


# In[57]:


sum_f(my_list, lambda x : x*x)


# In[58]:


sum_f(my_list, lambda x : x % 2)


# In[59]:


s = ['tiger', 'giraffe', 'cat', 'dog']


# In[60]:


s.sort


# In[61]:


s.sort()


# In[62]:


s


# In[63]:


list = [5,2,5,4,3]


# In[64]:


type(list)


# In[65]:


list.append(3)


# In[66]:


list


# In[67]:


list.sort()
list


# In[68]:


get_ipython().run_line_magic('pinfo', 'sort')


# In[69]:


get_ipython().run_line_magic('pinfo', 'list.sort')


# In[70]:


m = [[1,2,3], [4,5,6]]


# In[71]:


m


# In[72]:


m[0][1]


# In[73]:


t = (4,5,6)


# In[74]:


type(t)


# In[75]:


t = [4,5,6]


# In[76]:


type(t)


# In[77]:


t = (4,5,6)


# In[78]:


a, b, c = t


# In[82]:


a, *kk = t


# In[83]:


a


# In[84]:


kk


# In[85]:


a, *_ = t


# In[86]:


_


# In[87]:


list = [5,2,8,9,6]


# In[89]:


for i , x in enumerate(list):
    print(i, x)


# In[90]:


x = [2,4,6]; y = [100,200,300]


# In[91]:


for a, b in zip(x, y):
    print(a, b)


# In[93]:


d = {'한국' : '서울', '일본' : '도쿄', '중국' : '베이징'}


# In[94]:


type(d)


# In[95]:


d['중국']


# In[96]:


d['영국'] = '파리'


# In[97]:


d


# In[98]:


del d['일본']


# In[99]:


d


# In[100]:


d.keys()


# In[101]:


d.values()


# In[102]:


d['한국'] = 'seoul'


# In[103]:


d


# In[104]:


s1 = {1,2,3,3}


# In[105]:


s1


# In[106]:


s2 = {2,3,4}


# In[107]:


s1.union(s2)


# In[108]:


s1.intersecition(s2)


# In[109]:


s1.intersection(s2)


# In[114]:


x = [a for a in range(5)]


# In[115]:


x


# In[116]:


def squares(n=10):
    for i in range(1, n+1):
        yield i ** 5


# In[117]:


for x in squares(5):


# In[118]:


for x in squares(5):
    print(x)


# In[119]:


for x in squares(5):
    print(x)


# In[ ]:





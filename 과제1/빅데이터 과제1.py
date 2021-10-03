#!/usr/bin/env python
# coding: utf-8

# # 빅데이터 분석
# ## 201758101 배성규 
# ---
# 
# 

# In[123]:


# 1번 
def unzip(data):
    x, y = zip(*data)
    return x, y
def get_data():
    data = [ (3,6), (2.1, 5), (9.3, 10), (4,2), (-2, 7)]
    x, y = unzip(data)
    print(x)
    print(y)
get_data()


# In[124]:


# 2번
import keyword

def keyword_count(filename):
    dict = {}
    data = keyword.kwlist
    infile = open(filename, 'r')
    for line in infile:
        line_replace = line.replace(':',' ')
        line_split = line_replace.split()
        for word in line_split:
            if word in data:
                if word in dict:
                    dict[word] += 1
                else:
                    dict[word] = 1
                    
    return sorted(dict.items(), key = lambda x:x[1], reverse = True)

print(keyword_count('mystery.py'))


# In[125]:


# 3번 
import math

class RegularPolygon:
    """
    
        정다각형 (등변 & 등각) 
    
        parameters
        --------------
        n : int, default : 3
           변의 개수 
        s : float , default  : 1.0
            변의 길이 
    """
    #초기화
    def __init__(self, n = 3, s = 1.0):
        self.n = n
        self.s = s
    
    #getter & setter 
    def get_n(self):
        return self.n
    def set_n(self, n):
        self.n = n
    def get_s(self):
        return self.s
    def set_s(self, s):
        self.s = s
        
    #내각을 반환하는 메소드
    def getIntAngle(self):
        return 180 * (self.n -2) / self.n
    
    #둘레를 반환하는 메소드
    def getPerimeter(self):
        return self.n * self.s
    
    #면적을 반환하는 메소드 
    def getArea(self):
        return (self.n * (self.s ** 2)) / (4 * math.tan(math.pi / self.n))
    
    
RegularPolygon1 = RegularPolygon(6,3)
print('변의 개수 = ', RegularPolygon1.get_n())
print('변의 길이 = ', RegularPolygon1.get_s())
print('내각 = ', RegularPolygon1.getIntAngle())
print('둘레 = ', RegularPolygon1.getPerimeter())
print('면적 = ',RegularPolygon1.getArea())
print('------------------------------------')

RegularPolygon2 = RegularPolygon(4,)
print('변의 개수 = ', RegularPolygon2.get_n())
print('변의 길이 = ', RegularPolygon2.get_s())
print('내각 = ', RegularPolygon2.getIntAngle())
print('둘레 = ', RegularPolygon2.getPerimeter())
print('면적 = ',RegularPolygon2.getArea())
print('------------------------------------')

RegularPolygon3 = RegularPolygon()
RegularPolygon3.s = 5
print('변의 개수 = ', RegularPolygon3.get_n())
print('변의 길이 = ', RegularPolygon3.get_s())
print('내각 = ', RegularPolygon3.getIntAngle())
print('둘레 = ', RegularPolygon3.getPerimeter())
print('면적 = ',RegularPolygon3.getArea())


# In[126]:


get_ipython().run_line_magic('pinfo', 'RegularPolygon')


# In[ ]:





# In[ ]:





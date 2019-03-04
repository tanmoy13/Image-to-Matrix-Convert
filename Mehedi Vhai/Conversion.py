
# coding: utf-8

# In[2]:


import cv2


# In[28]:


import csv, numpy as np


# In[31]:


path = "G:\Work\data"


# In[34]:


x=0


# In[ ]:


with open(path+'\\test.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        arr=np.array(row)
        img=np.reshape(arr,(28,28))
        with open(path+"\\"+str(x)+".png", 'wb') as fd:
            fd.write(img)
        x+=1


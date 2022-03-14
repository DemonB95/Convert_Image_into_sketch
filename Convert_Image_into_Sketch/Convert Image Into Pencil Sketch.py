#!/usr/bin/env python
# coding: utf-8

# In[192]:


import numpy as np
import imageio
import scipy.ndimage
import cv2


# In[193]:


img= "virat.jpg"


# In[194]:


def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.2989,0.5870,0.1140]) #to convert image into gray scale 


# In[195]:


def dodge(front,back):
    final_sketch=front*255/(255-back)# if image is grater tha 255 then it will make it 255
    final_sketch[final_sketch>255]==255 
    final_sketch[back==255]=255
    return final_sketch.astype('uint8')


# In[196]:


ss=imageio.imread(img)#to read


# In[197]:


gray=rgb2gray(ss)


# In[198]:


i=255-gray #0,0,0 for darkest color and 255 ,255,255 for brightest


# In[199]:


# to convert into blur image
blur=scipy.ndimage.filters.gaussian_filter(i,sigma=15)
#sigma is intensity of blurness


# In[200]:


r=dodge(blur,gray)#this will covert image into sketch


# In[201]:


cv2.imwrite('virat_sketch.png',r)


# In[ ]:





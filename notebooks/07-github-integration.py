
# coding: utf-8

# In[1]:

# %install_ext https://raw.githubusercontent.com/rasbt/watermark/master/watermark.py
get_ipython().magic(u'load_ext watermark')
get_ipython().magic(u'watermark --githash --machine --python --packages pandas,numpy,matplotlib -u --custom_time %Y-%m-%d')


# In[2]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
import seaborn as sns
sns.set();


# In[3]:

x = np.random.random_sample(100) * 50.0


# In[4]:

y = np.sin(x)


# In[5]:

plt.scatter(x, y)


# In[6]:

plt.plot(x,y)


# In[ ]:




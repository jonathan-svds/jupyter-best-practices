
# coding: utf-8

# In[2]:

# %install_ext https://raw.githubusercontent.com/rasbt/watermark/master/watermark.py
get_ipython().magic(u'load_ext watermark')
get_ipython().magic(u'watermark --githash --machine --python --packages pandas,numpy,matplotlib -u --custom_time %Y-%m-%d')


# In[3]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
import seaborn as sns
sns.set();


# In[4]:

x = np.random.random_sample(100) * 50.0


# In[5]:

y = np.sin(x)


# In[6]:

plt.scatter(x, y)


# In[8]:

# Create new visualization


# In[9]:

plt.scatter(x,y**2.0)


# In[ ]:




# In[ ]:




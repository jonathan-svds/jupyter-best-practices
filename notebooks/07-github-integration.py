
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


# In[11]:

x = np.random.random_sample(1000) * 50.0


# In[12]:

y = np.sin(x)


# In[13]:

plt.scatter(x, y)


# In[14]:

# Create new visualization


# In[15]:

plt.scatter(x,y**2.0, color='red')


# In[16]:

plt.scatter(x,y**2.0, color='red')


# In[ ]:




# In[ ]:





# coding: utf-8

# In[8]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
import seaborn as sns
sns.set();


# In[5]:

x = np.random.random_sample(100) * 50.0


# In[6]:

y = np.sin(x)


# In[9]:

plt.scatter(x, y)


# In[ ]:




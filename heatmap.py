
# coding: utf-8

# In[22]:


import folium
from folium import plugins
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('./cellid.csv', nrows=100)
print(data.sample(10))
longitude_lim=(data['longitude'].min(),data['longitude'].max())
latitude_lim=(data['latitude'].min(),data['latitude'].max())
print(longitude_lim, latitude_lim)


# In[60]:


m = folium.Map(location=[40.830429, -73.891762], zoom_start=11)


# In[61]:


data['latitude'] = data['latitude'].astype(float)
data['longitude'] = data['longitude'].astype(float)


# In[62]:


heat_data = [[row['latitude'],row['longitude']] for index, row in data.iterrows()]


# In[63]:


# plugins.HeatMap(heat_data).add_to(m)
#
m = folium.Map([40.830429, -73.891762],tiles='Stamen Toner', zoom_start=11)
m.add_child(plugins.HeatMap(heat_data, radius = 8))


# In[64]:

m.save('./heat_map.html')


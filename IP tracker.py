#!/usr/bin/env python
# coding: utf-8

# In[38]:


import os
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import json

def getapi():
    while True:
        ip = input("Enter your targeted IP address")
        url = "http://ip-api.com/json/"
        response=urllib.request.urlopen(url+ ip)
        dataset = response.read()
        val = json.loads(dataset) #decode the data and stores in val

        print("IP: " + val["query"])
        print("ISP: " + val["isp"])
        print("Country: " + val["country"])
        print("City: " + val["city"])
        print("ZIP Code: " + str(val["zip"]))
        print("Latitude: " + str(val["lat"]))
        print("Longitude: " + str(val["lon"]))
        print("Timezone: " + val["timezone"])
        print("AS: " + val["as"])

        break
        
getapi()


# In[ ]:





# In[ ]:





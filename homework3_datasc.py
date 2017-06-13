
# coding: utf-8

# In[1]:

import pandas as pd
url = ["http://rates.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/01/12-00", "http://rates.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/02/12-00","http://rates.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/03/12-00","http://rates.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/04/12-00","http://rates.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/05/12-00", "http://rates.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/06/12-00", "http://rates.am/am/armenian-dram-exchange-rates/banks/non-cash/2017/06/07/12-00"]
for day in url:
    ex_rate = pd.read_html(day)
    data = ex_rate[2]
    print data[2:19]




# In[16]:

import re
import requests
url="https://www.bloomberg.com/quote/SPX:IND"
response_bloom = requests.get(url)


# In[21]:

SP500=response_bloom.text
from pprint import pprint
pprint(response_bloom)
data= re.sub(r'<|>'," ",SP500)
output=re.findall('"price"\s*([0-9]\S*)',data)
print output[0]


# In[23]:

import json
input='''[
    {
    "Movie":"Game of Thrones",
    "Actor":"Peter Dinklage",
    "Role":"Tyrion Lannister"    
    },
    {
    "Movie":"Vikings",
    "Actor":"Travis Fimmel",
    "Role":"Ragnar Lothbrok"  
    },
    {
    "Movie":"The last Kingdom",
    "Actor":{
            "Young Uhtred":"Tom Taylor",
            "Not that young Uhtred":"Alexander Dreymon"
            },
    "Role":"Uhtred of Bebbanburg"
    }
]'''


# In[24]:

movies = json.loads(input)
from pprint import pprint
pprint(movies)


# In[25]:

for movie in movies:
            print('Movie: ', movie['Movie'])
            print('Role: ', movie['Role'])
            if type(movie['Actor'])== dict:
                    print('Actor 1: ', movie['Actor']['Young Uhtred'])
                    print('Actor 2: ', movie['Actor']['Not that young Uhtred'])
            else:
                print('Actor: ', movie['Actor'], "\n")


# In[28]:

import pandas as pd
import matplotlib.pyplot as plt


# In[35]:

passangers = pd.read_csv("AirPassengers.csv")
print passangers.head(144)
plt.plot(passangers['Passengers'])
plt.show()


# In[36]:

import re
import requests
url="http://quotes.toscrape.com/"
response=requests.get(url)


# In[37]:

data=response.text
output=re.findall("href=\s*(\S*)\s*next",data,re.IGNORECASE)
print "http://quotes.toscrape.com"+output[0]


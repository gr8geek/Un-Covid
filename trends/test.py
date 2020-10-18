import pandas as pd                        
from pytrends.request import TrendReq
pytrend = TrendReq()
pytrend.build_payload(kw_list=["Taylor Swift", "Covid"])
# Interest by Region
df = pytrend.interest_by_region()
print(df.head(10))

covid = pytrend.build_payload(kw_list=['Coronavirus'])

inp = input("1. US \n2. India ")
if int(inp)==1:
    geo="US"
else:
    geo="IN"
import requests
from bs4 import BeautifulSoup

URL = "https://trends.google.com/trends/?geo="+geo
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup)

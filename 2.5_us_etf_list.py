from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_American_exchange-traded_funds"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')
rows = soup.select('div > ul > li')

etfs = {}
for row in rows:
    try:
        etf_name = re.findall('^(.*) \(NYSE', row.text)
        etf_market = re.findall('\((.*)\|', row.text)
        etf_ticker = re.findall('NYSE Arca\|(.*)\)', row.text)

        if (len(etf_ticker) > 0) & (len(etf_market) > 0):
            etfs[etf_ticker[0]] = [etf_market[0], etf_name[0]]

    except AttributeError as err:
        pass

print(etfs)
print('\n')

df = pd.DataFrame(etfs)
print(df)
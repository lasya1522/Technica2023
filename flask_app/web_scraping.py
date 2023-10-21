#web scraping file
from bs4 import BeautifulSoup
import requests
import pandas as pd

from urllib.request import urlopen
from urllib.error import HTTPError, URLError


def parseURL(url):
    try:
        html = urlopen(url)
        soup = BeautifulSoup(html.read(), 'html.parser')
    except HTTPError as e:
        print("The server returned an HTTP error")
    except URLError as e:
        print("The server could not be found!")
    else:
        print("Access granted")
    
    table_rows = soup.find_all('tr', attrs={'class':'alt'})
    print(len(table_rows))

    res = []
    for ind in range(0, len(table_rows)-1, 2):
        tr = table_rows[ind]
        loc = table_rows[ind+1]
        td = tr.find_all('td')
        row = [x.text.strip() for x in td if x.text.strip()]
        td = loc.find_all('td')
        loc = [x.text.strip() for x in td if x.text.strip()]
        row.append(loc[0])
        if row:
            res.append(row)

    return res

final = []
for year in range(2016, 2024):
    for month in range(1, 13):
        #if year < 2023 or (year == 2023 and month < 11):
        final += parseURL("https://www.umpd.umd.edu/stats/csa_logs.cfm?year={}&month={}".format(year, month))
        print(year, month)

df = pd.DataFrame(final, columns=["Delete_na", "Time_of_Incident", "Time_of_report", "Incident", "Delete_disposition", "Location"])
df.to_csv("crime_data.csv")
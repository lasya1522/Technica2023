#web scraping file
from bs4 import BeautifulSoup
import requests
import pandas as pd

from urllib.request import urlopen
from urllib.error import HTTPError, URLError

html = urlopen('https://www.umpd.umd.edu/stats/csa_logs.cfm')
print(html.read())

def parseURL(url):
    # parse text
    soup = BeautifulSoup(html.read(), 'html.parser')
    # print(soup.prettyfy())

    try:
        html = urlopen("https://www.umpd.umd.edu/stats/csa_logs.cfm")
    except HTTPError as e:
        print("The server returned an HTTP error")
    except URLError as e:
        print("The server could not be found!")
    else:
        print(html.read())
    
    table = soup.find('table', attrs={'class':'subs noBorders evenRows'})
    table_rows = table.find_all('tr')

    res = []
    for tr in table_rows:
        td = tr.find_all('td')
        row = [tr.text.strip() for tr in td if tr.text.strip()]
        if row:
            res.append(row)

    df = pd.DataFrame(res, columns=["OCCURRED DATE TIME LOCATION", 
                                "REPORT DATE", "NATURE (CLASSIFICATION)"])
    print(df)


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)
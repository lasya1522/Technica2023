#web scraping file
from bs4 import BeautifulSoup
import requests

from urllib.request import urlopen
from urllib.error import HTTPError, URLError

html = urlopen('https://www.umpd.umd.edu/stats/csa_logs.cfm')
print(html.read())

# parse text
soup = BeautifulSoup(html.read(), 'html.parser')
print(soup.prettyfy())

try:
    html = urlopen("https://www.umpd.umd.edu/stats/csa_logs.cfm")
except HTTPError as e:
    print("The server returned an HTTP error")
except URLError as e:
    print("The server could not be found!")
else:
    print(html.read())


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
import requests
import re
from bs4 import BeautifulSoup

def gethtml(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "It is failed to get html!"

def getcontent(url):
    html = gethtml(url)
    bsObj = BeautifulSoup(html,"html.parser")
    print(bsObj.prettify)


if __name__ == '__main__':
    url = "http://www.pythonscraping.com/pages/page3.html"
    getcontent(url)

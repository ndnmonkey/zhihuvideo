from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

def get_html(url):
    browser.get(url)
    print(browser.page_source)
    return browser.page_source
def content_print(pagesource):
    soup = BeautifulSoup(pagesource,"html.parser")

if __name__ == '__main__':
    browser = webdriver.Chrome()
    initial_url = "https://www.zhihu.com/question/21086211"
    html = get_html(initial_url)
    content_print(html)
    browser.close()

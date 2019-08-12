from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import csv



def get_html(url):
    browser.get(url)
    return browser.page_source
def content_print(pagesource):
    soup = BeautifulSoup(pagesource,"html.parser")
    films = soup.find_all("dd")
    film_list= []
    for film in films:
        name =film.find("a")
        haha =name["title"]
        #print(haha)

        stars =film.find("p",class_ = "star")
        #print(stars.text)

        date = film.find("p",class_ = "releasetime").string


        score_1 = film.find("i",class_ = "integer")
        score_2 = film.find("i",class_ = "fraction")
        score = score_1.text + score_2.text
        #print(score)
        film_list.append([haha,date,score])
    print(film_list)



if __name__ == '__main__':
    browser = webdriver.Chrome()
    for i in range(0,10):
        houzhui = str(10 * i)

        initial_url = "http://maoyan.com/board/4?offset="  + houzhui
        html = get_html(initial_url)
        content_print(html)

    browser.close()

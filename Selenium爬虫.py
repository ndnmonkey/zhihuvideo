'''这个版本能够爬出拥有10页的电影信息的具体信息，
并将这些信息写在Excel中。整个过程是批量化的，输入参数无需干预。'''

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
    infos= []
    for film in films:
        name =film.find("a")
        haha =name["title"]
        #print(haha)

        stars =film.find("p",class_ = "star")
        #print(stars.text)

        date1 = film.find("p",class_ = "releasetime").string
        date = date1.split("：")[1]
        print(date)

        score_1 = film.find("i",class_ = "integer")
        score_2 = film.find("i",class_ = "fraction")
        score = score_1.text + score_2.text
        #print(score)
        infos.append([haha,date,score])
    #print(infos)

    list = []
    for x in range(0, 10):
        for y in range(0, 3):
            # print(infos[x][y])
            list.append(infos[x][y])
    # print(list)

    names = []
    for n in range(0, 30, 3):
        for i in range(n, n + 3):
            # print(list[i])
            names.append(list[i])
        #print(names)

        # csv 写入
        #names = ['marry', 26]

        # 打开文件，追加a
        out = open('C:/Users/zhengyong/Desktop/csv.csv', 'a', newline='')
        # 设定写入模式
        csv_write = csv.writer(out, dialect='excel')
        # 写入具体内容
        csv_write.writerow(names)
        print(str(n / 3) + "  times to write in the Excel!")
        names = []

if __name__ == '__main__':
    browser = webdriver.Chrome()
    for i in range(0,10):
        houzhui = str(10 * i)
        initial_url = "http://maoyan.com/board/4?offset="  + houzhui
        html = get_html(initial_url)
        content_print(html)
    browser.close()

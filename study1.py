import pandas as pd
import csv

infos = [['霸王别姬', '上映时间：1993-01-01(中国香港)', '9.6'], ['肖申克的救赎', '上映时间：1994-10-14(美国)', '9.5'], ['罗马假日', '上映时间：1953-09-02(美国)', '9.1'], ['这个杀手不太冷', '上映时间：1994-09-14(法国)', '9.5'], ['教父', '上映时间：1972-03-24(美国)', '9.3'], ['泰坦尼克号', '上映时间：1998-04-03', '9.5'], ['龙猫', '上映时间：1988-04-16(日本)', '9.2'], ['唐伯虎点秋香', '上映时间：1993-07-01(中国香港)', '9.2'], ['魂断蓝桥', '上映时间：1940-05-17(美国)', '9.2'], ['千与千寻', '上映时间：2001-07-20(日本)', '9.3']]


list = []
for x in range(0,10):
    for y in range(0,3):
        #print(infos[x][y])
        list.append(infos[x][y])
#print(list)

names = []
for n in range(0,30,3):
    for i in range(n,n+3):
        #print(list[i])
        names.append(list[i])
    print(names)

    # csv 写入
    #names = ['marry', 26]
    # 打开文件，追加a
    out = open('C:/Users/zhengyong/Desktop/study/Stu_csv.csv', 'a', newline='')

    # 设定写入模式
    csv_write = csv.writer(out, dialect='excel')
    # 写入具体内容
    csv_write.writerow(names)
    print(  str(n/3) + "times to write in the Excel!")
    names = []




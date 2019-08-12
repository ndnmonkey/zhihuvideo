import pandas as pd

infos = [['霸王别姬', '上映时间：1993-01-01(中国香港)', '9.6'], ['肖申克的救赎', '上映时间：1994-10-14(美国)', '9.5'], ['罗马假日', '上映时间：1953-09-02(美国)', '9.1'], ['这个杀手不太冷', '上映时间：1994-09-14(法国)', '9.5'], ['教父', '上映时间：1972-03-24(美国)', '9.3'], ['泰坦尼克号', '上映时间：1998-04-03', '9.5'], ['龙猫', '上映时间：1988-04-16(日本)', '9.2'], ['唐伯虎点秋香', '上映时间：1993-07-01(中国香港)', '9.2'], ['魂断蓝桥', '上映时间：1940-05-17(美国)', '9.2'], ['千与千寻', '上映时间：2001-07-20(日本)', '9.3']]


list = []
for x in range(0,10):
    for y in range(0,3):
        #print(infos[x][y])
        list.append(infos[x][y])
names = []
for name in range(0,30,3):
    names.append(list[name])
#print(names)

dates = []
for date in range(1,30,3):
    dates.append(list[date])
#print(dates)

grades = []
for grade in range(2,30,3):
    grades.append(list[grade])
#print(grades)

dateframe = pd.DataFrame({'Movies':names,'Dates':dates,'Scores':grades})
#输出顺序是怎样的？为什么不是按照我设置的顺序？
dateframe.to_csv('C:/Users/zhengyong/Desktop\/study/csv.csv',index=False,sep=',',encoding = "gbk")



import csv

#csv 写入
stu1 = ['marry',26]
stu2 = ['bob',23]
#打开文件，追加a
out = open('C:/Users/zhengyong/Desktop/study/Stu_csv.csv','a', newline='')

#设定写入模式
csv_write = csv.writer(out,dialect='excel')
#写入具体内容
csv_write.writerow(stu1)
csv_write.writerow(stu2)



print ("write over")

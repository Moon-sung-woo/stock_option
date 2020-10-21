#날짜, 시가, 고가, 저가, 종가, 거래량, MA, SD, UBB, LBB
import csv

file_name = 'test.csv'
day = 10
count = 0
trainX = []

f = open(file_name, 'r', encoding='utf-8-sig')
lines = csv.reader(f)
lines = list(lines)
lines = lines[2:1000]
#print(lines)
for line in lines:
    count += 1
    if int(line[4]) < float(line[9]): # 볼린저 밴드보다 종가가 적으면
        temp = []
        escape_bll = lines[count-day:count]
        print(escape_bll)
        temp.append(escape_bll)

#카운트를 어디서 해줘야 할지 생각해보기!
print(count)
f.close()
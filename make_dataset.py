
#날짜, 시가, 고가, 저가, 종가, 거래량, MA, SD, UBB, LBB
import csv

file_name = 'test.csv'
count = 0
trainX = []

f = open(file_name, 'r', encoding='utf-8-sig')
lines = csv.reader(f)
lines = list(lines)
lines = lines[2:100]
print(lines)
for line in lines:
    if line[4] < line[9]: # 볼린저 밴드보다 종가가 적으면
        pass
    count += 1

print(count)
f.close()
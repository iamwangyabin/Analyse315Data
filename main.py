import csv


# 读取csv至字典/home/wang/workspace/Analyse315Data/wang3 (1).csv
csvFile = open("wang3 (2).csv", "r")
reader = csv.reader(csvFile)

result = []
for item in reader:
    # 忽略第一行
    if reader.line_num == 1:
        continue
    result.append(item[2])

import pkuseg

seg = pkuseg.pkuseg()                                  # 以默认配置加载模型


data={}

for i in result:
    text = seg.cut(i)
    for u in text:
        if u in data.keys():
            data[u]+=1
        else:
            data[u]=1

d=sorted(data.items(), key=lambda x: x[1], reverse=True)

f = open('dict.csv','wb')
w = csv.DictWriter(f,d.keys())
w.writerow(d)
f.close()

with open("test.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    #先写入columns_name
    writer.writerow(["字","频数"])
    #写入多行用writerows
    for i in d:
        i=list(i)
        i[1]=str(i[1])
        writer.writerow(i)

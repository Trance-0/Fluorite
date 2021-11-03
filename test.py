import csv
import random
import math
price_queue=[]
# awsome tool: https://trendinsight.oceanengine.com/arithmetic-index
x=[]
y=[]
with open('ETH-CNY.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'date = {row[0]} High = {row[2]} Low = {row[3]} Volume = {row[6]}.')
            date=row[0]
            volume=row[6]
            tik_tok=row[7]

            price=random.randrange(math.ceil(float(row[3])),math.floor(float(row[2])))
            y.append(price)
            x.append([volume,tik_tok])
            line_count += 1
    print(f'Processed {line_count} lines.')

print (x)
print (y)
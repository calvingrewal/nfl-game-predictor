import csv

with open('sfo.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)
    print(headers)
    print('*******************')
    for row in reader:
        print(row)

f.close()
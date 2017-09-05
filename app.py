import csv

opponent = 'San Francisco 49ers'

with open('ram.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)

    opponentIndex = headers.index('Opp')
    for row in reader:
        if row[opponentIndex] == opponent:
            print(row)

f.close()
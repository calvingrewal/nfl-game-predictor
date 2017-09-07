import csv
import json

teamData = None
with open('teams.json') as f:
    teamData = json.load(f)

team = 'sfo'
opponent = 'sea'

with open(team+'.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)

    opponentIndex = headers.index('Opp')
    opponentId = teamData["teamname"][opponent]

    for row in reader:
        if row[opponentIndex] == teamData["id"][opponentId]:
            print(row)

f.close()
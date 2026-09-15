import csv
file = open("2526.csv","r",newline="")
reader = csv.reader(file)
next(reader)
gScoredArsenal=0
countArsenal=0
gConcArsenal=0
for row in reader:
    homeGoals = float(row[5])
    awayGoals = float(row[6])
    if row[3] == "Arsenal":
        gScoredArsenal+=homeGoals
        gConcArsenal+=awayGoals
        countArsenal+=1
    elif row[4] == "Arsenal":
        gScoredArsenal+=awayGoals
        countArsenal+=1
        gConcArsenal+=homeGoals
print("goals for per game:", round(gScoredArsenal/countArsenal,2))
print("goals against per game:", round(gConcArsenal/countArsenal,2))
### attack strength and def strength

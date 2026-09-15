import csv
file = open("2526.csv","r",newline="")
reader = csv.reader(file)
next(reader)
goalsArsenal=0
countArsenal=0
for row in reader:
    homeGoals = float(row[5])
    awayGoals = float(row[6])
    if row[3] == "Arsenal":
        goalsArsenal+=homeGoals
        countArsenal+=1
    elif row[4] == "Arsenal":
        goalsArsenal+=awayGoals
        countArsenal+=1
print("goals per game:", round(goalsArsenal/countArsenal,2))
#### calculates arsenals attack strength which is part of the poisson formula

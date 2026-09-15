import csv
file = open("2526.csv","r",newline="")
reader = csv.reader(file)
next(reader)
goalsArsenal=0
for row in reader:
    homeGoals = float(row[5])
    awayGoals = float(row[6])
    if row[3] == "Arsenal":
        goalsArsenal+=homeGoals
    elif row[4] == "Arsenal":
        goalsArsenal+=awayGoals
print(goalsArsenal)
### shows that I can make use of the values in the csv, obviously not fully developed yet but for documentation purposes
##reason the file is different to the github one is beacuse i am coding through idle rather than codespace since i cant figure visualstudio out

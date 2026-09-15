import csv
file = open("csvTeachMyself/teams.csv","r",newline="")
reader = csv.reader(file)
next(reader)
for row in reader:
    attack = float(row[1])
    defence = float(row[2])
    print(row[0],attack,defence)
## Now attack and defence strengths are numbers instead of strings

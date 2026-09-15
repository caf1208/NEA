import csv
file = open("csvTeachMyself/teams.csv","r",newline="")
reader = csv.reader(file)
next(reader)     #    skips the first line ie the header
for row in reader:
    print(row[0],"has an attack strength of", row[1])

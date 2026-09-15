import csv
file = open("csvTeachMyself/teams.csv","r",newline="")
reader = csv.reader(file)
for row in reader:
    if row !=1:
        print(row[0],"has an attack strength of", row[1])   #  trying to print without it printing headers

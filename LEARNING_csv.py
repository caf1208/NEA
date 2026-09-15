import csv
file = open("csvTeachMyself/teams.csv","r",newline="")
reader = csv.reader(file)
next(reader)
for row in reader:
    team = row[0]
    attack = float(row[1])
    defence = float(row[2])
    print(f"{team}: \n attack ={attack} \n defence ={defence}")
## my way of learning new line at the same time as doing what i did before

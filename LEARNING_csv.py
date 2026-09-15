import csv
file = open("csvTeachMyself/teams.csv","r",newline="")
reader = csv.reader(file)
for row in reader:
  print(row)

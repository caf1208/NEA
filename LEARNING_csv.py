import csv
file = open(teamsLEARNING.csv,"r",newline="")
reader = csv.reader(file)
for row in reader:
  print(row)

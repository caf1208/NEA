import csv
file = open("2526.csv","r",newline="")
reader = csv.reader(file)
next(reader)
count = 0
for row in reader:
    if row[3] == "Arsenal" or row[4] == "Arsenal":
        count +=1
print(f"Arsenal played {count} games")

### i plan to document it but it is here too just incase it needs to be

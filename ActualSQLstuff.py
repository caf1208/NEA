import sqlite3
import csv
file=open("2526.csv","r",newline="")
reader=csv.reader(file)
next(reader)
con=sqlite3.connect("DATABASE.db")
cur=con.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS matches(
    id INTEGER PRIMARY KEY,
    homeTeam TEXT,
    awayTeam TEXT,
    homeGoals INTEGER,
    awayGoals INTEGER
)
""")
con.commit()
for row in reader:
    goalsHome=int(row[5])
    goalsAway=int(row[6])
    cur.execute("""
INSERT INTO matches VALUES (?,?,?,?)
""",(row[3],row[4],goalsHome,goalsAway))
con.commit()
con.close()


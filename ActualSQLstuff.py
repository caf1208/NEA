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
cur.execute("""
SELECT COUNT(*) FROM matches WHERE homeTeam="Arsenal"
""")
homeGames=cur.fetchone()[0]
cur.execute("""
SELECT COUNT(*) FROM matches WHERE awayTEAM="Arsenal"
""")
awayGames=cur.fetchone()[0]
cur.execute("""
SELECT SUM(homeGoals) FROM matches WHERE homeTeam="Arsenal"
""")
homeGoalsF=cur.fetchone()[0]
cur.execute("""
SELECT SUM(awayGoals) FROM matches WHERE homeTeam="Arsenal"
""")
homeGoalsA=cur.fetchone()[0]
cur.execute("""
SELECT SUM(awayGoals) FROM matches WHERE awayTeam="Arsenal"
""")
awayGoalsF=cur.fetchone()[0]
cur.execute("""
SELECT SUM(homeGoals) FROM matches WHERE awayTeam="Arsenal"
""")
awayGoalsA=cur.fetchone()[0]
print(f"""
Home Goals Scored avg: {round(homeGoalsF/homeGames,2)}
Home Goals Conceded avg: {round(homeGoalsA/homeGames,2)}
Away Goals Scored avg: {round(awayGoalsF/awayGames,2)}
Away Goals Conceded avg: {round(awayGoalsA/awayGames,2)}
""")
con.close()
#in process of doing same using sql as with csv

import sqlite3
import csv
file=open("2526.csv","r",newline="")
reader=csv.reader(file)
next(reader)
con=sqlite3.connect("DATABASE.db")
cur=con.cursor()
def chooseTeam(teams):
    team=input("Which team")
    for i in teams:
        if i.lower()==team.lower():
            return i
    return chooseTeam(teams)


teams=[]
for row in reader:
    if row[3] not in teams:
        teams.append(row[3])
    if row[4] not in teams:
        teams.append(row[4])
file.seek(0)
reader=csv.reader(file)
next(reader)

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
team = chooseTeam(teams)
cur.execute("""
SELECT
    COUNT(CASE WHEN homeTeam=? THEN 1 END),
    COUNT(CASE WHEN awayTeam=? THEN 1 END),
    SUM(CASE WHEN homeTeam=? THEN homeGoals ELSE 0 END),
    SUM(CASE WHEN homeTeam=? THEN awayGoals ELSE 0 END),
    SUM(CASE WHEN awayTeam=? THEN awayGoals ELSE 0 END),
    SUM(CASE WHEN awayTeam=? THEN homeGoals ELSE 0 END),
    COUNT(*),
    SUM(homeGoals),
    SUM(awayGoals)
FROM matches
""",(team,team,team,team,team,team))
result=cur.fetchone()
homeGames=result[0]
awayGames=result[1]
homeGoalsF=result[2]
homeGoalsA=result[3]
awayGoalsF=result[4]
awayGoalsA=result[5]
games=result[6]
leagueHomeGoals=result[7]
leagueAwayGoals=result[8]
print(f"""
Home Goals Scored avg: {round(leagueHomeGoals/games,2)}
Home Goals Conceded avg: {round(leagueAwayGoals/games,2)}
Away Goals Scored avg: {round(leagueAwayGoals/games,2)}
Away Goals Conceded avg: {round(leagueHomeGoals/games,2)}

{team}:

home attack strength: {round((homeGoalsF/homeGames)/(leagueHomeGoals/games),2)}
home defence strength: {round((homeGoalsA/homeGames)/(leagueAwayGoals/games),2)}
away attack strength: {round((awayGoalsF/awayGames)/(leagueAwayGoals/games),2)}
away defense strength: {round((awayGoalsA/awayGames)/(leagueHomeGoals/games),2)}
""")
con.close()

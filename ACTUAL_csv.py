import csv
file = open("2526.csv","r",newline="")
reader = csv.reader(file)
next(reader)
"""
gScoredArsenal=0
countArsenal=0
gConcArsenal=0
homeGoals=0
gamesTotal=0
for row in reader:
    """"""
    homeGoals = float(row[5])
    awayGoals = float(row[6])
    if row[3] == "Arsenal":
        gScoredArsenal+=homeGoals
        gConcArsenal+=awayGoals
        countArsenal+=1
    elif row[4] == "Arsenal":
        gScoredArsenal+=awayGoals
        countArsenal+=1
        gConcArsenal+=homeGoals
print("goals for per game:", round(gScoredArsenal/countArsenal,2))
print("goals against per game:", round(gConcArsenal/countArsenal,2))
""""""
    gamesTotal+=1
    homeGoals+=float(row[5])
print("home goals per game:", round(homeGoals/gamesTotal,2))
"""
def chooseTeam(teams):
    team=input("Which team")
    if team.lower() in teams:
        return team.lower()
    else:
        return chooseTeam(teams)
def calculateTeamStrengths(team,reader):
    teamHGames=0
    teamHGoalsF=0
    teamHGoalsA=0
    teamAGames=0
    teamAGoalsF=0
    teamAGoalsA=0
    games=0
    AGoals=0
    HGoals=0
    for row in reader:
        hg=int(row[5])
        ag=int(row[6])
        games+=1
        AGoals+=ag
        HGoals+=hg
        if team==row[3].lower():
            teamHGames+=1
            teamHGoalsF+=hg
            teamHGoalsA+=ag
        elif team==row[4].lower():
            teamAGames+=1
            teamAGoalsF+=ag
            teamAGoalsA+=hg
    avgH=HGoals/games
    avgA=AGoals/games
    print(f"""
league away avg goals: {round(avgA,2)}
league home avg goals: {round(avgH,2)}

{team.capitalize()}:

home attack strength: {round((teamHGoalsF/teamHGames)/avgH,2)}
home defense strength: {round((teamHGoalsA/teamHGames)/avgA,2)}
away attack strength: {round((teamAGoalsF/teamAGames)/avgA,2)}
away defence strength: {round((teamAGoalsA/teamAGames)/avgH,2)}
""")
teams=[]
for row in reader:
    if row[3].lower() not in teams:
        teams.append(row[3].lower())
    if row[4].lower() not in teams:
        teams.append(row[4].lower())
file.seek(0)
reader=csv.reader(file)
next(reader)
calculateTeamStrengths(chooseTeam(teams),reader)
##I dont know if anything changed but this is a definite working solution to find out the values, I may use may not use depends how 
#quickly I finish the more basic NEA and then I can make it more complicated

        

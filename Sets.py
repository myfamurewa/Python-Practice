nba_teams = {"Pistons", "Bucks", "Bulls", "Pacers", "Grizzlies", "Raptors"}
# sets aren't ordered so you can't call an element by it's index
# add elemeents to a set
nba_teams.add("Spurs")
nba_teams.add("Globetrotters")
# you can't edit values in a set

#remove and pop
nba_teams.remove("Globetrotters")
# remove removes the entry matching the name put into the function
nba_teams.pop()
# pop removes the last element

print(nba_teams)
print(len(nba_teams))
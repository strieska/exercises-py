file = open("boardgames.txt","r")
lines = file.read().split("\n")
games_played = 0
best_game = ["",0]
new_games = 0
for line in lines:
    line = line.split(";")
    games_played += int(line[2])
    if float(line[1])>float(best_game[1]):
        best_game[0] = line[0]
        best_game[1] = line[1]
    if int(line[3])>2010:
        new_games += 1
print(f"Total games played: {games_played}")
print(f"Best game: {best_game[0]} ({best_game[1]})")
print(f"Number of new games: {new_games}")
file.close()
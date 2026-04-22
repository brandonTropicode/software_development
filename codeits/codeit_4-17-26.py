# - Create a simple game tracking system using a dictionary
# - Create `games` dictionary where keys are individual games and values for those keys are the genres for those games
# - Create 2 functions:
#     - add_game(game, genre) → adds a game and its genre to the games dictionary
#     - get_games_by_genre(genre) → returns a list of all games that have the given genre
#     - Example

games = {
    # "key":value,
    # key = game name,
    # value = genre
}

# dictionary[key] = value -> this will add/update a key value pair at given key with a given value

# add_game: adds a game and its genre to the games dictionary
def add_game(game: str, genre: str):
    games[game] = genre
    
# get_games_by_genre: returns a list of all games that have the given genre
def get_games_by_genre(genre):
    result = []

    for game in games:
        if games[game] == genre:
            result.append(game)
    
    return result

print(f'Games dictionary before adding game\n{games}')

add_game("geomotrydash", "ss")
add_game("roblox", "rp")
add_game("fortnite", "tps")
add_game("cod", "fps")
print(f'Games dictionary after adding game\n{games}')

genre_input = input("What genre games do you want to find? ")
filtered_games = get_games_by_genre(genre_input)
print(filtered_games)
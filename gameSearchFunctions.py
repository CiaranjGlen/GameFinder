def find_game_by_name(csv_reader, gamedata, gametofind):
    gamesList = []
    gamereviews = []
    gamedata.seek(0)
    # iterate through the rows and if lowecase of user input matches lowercase of value in row[1] it will add to list
    for rows in csv_reader:
        if gametofind.lower() in rows[1].lower():
            gamesList.append(rows[1])
            gamereviews.append(rows[8])
    # returns a joint list where gamelist and gamre review values match
    return zip(gamesList, gamereviews)


# prints the input lists values in format (param will be output of findgameby name assigned to a var in gamefinder.py)
def print_matching_games(matching_games):
    for idx, (game_name, game_description) in enumerate(matching_games, start=1):
        print(f"Game #{idx}: {game_name}\n")
        print({game_description})
        print("\n" + "-" * 50 + "\n")  # Separation line


def navprompt():
    functionchoice = int(
        input(
            "1- search another game 2- search by genere 3- Search Games by rating 4- Review Findings 0 - Exit Program: "
        )
    )
    print(functionchoice)
    return functionchoice

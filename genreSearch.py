from pyfiglet import Figlet


# function with params for csv reader the csv file and chosen font for pyfiglet
def search_games_by_genre(csv_reader, gamedata, pygletfont):
    # resets reader to the top of file to make sure it reads all data
    gamedata.seek(0)
    generelist = []
    genres_input = input("What genres do you want to play? ")
    # split the input and add to list as seperate strings
    generelist.extend(genres_input.split())

    matching_games = False  # Flag to check if there are matching games

    for rows in csv_reader:
        # all keyword used to make sure both terms match genres for better matchign games
        if all(genre.lower() in rows[7].lower() for genre in generelist):
            matching_games = True  # Set the flag to True
            # renders output
            game_art = Figlet(font=pygletfont).renderText(rows[1])
            print(game_art)
            print(f"Genres: {rows[7]}")
            print(f"Summary: {rows[9]}\n")

    # Check if no matching games were found
    if not matching_games:
        print("No games found for the specified genres.")

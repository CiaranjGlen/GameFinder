import csv

# import all the functions for from the applications other modules
from sortbyratingmethods import (
    getGamesWithRating,
    sortDictHighToLow,
    sortDictLowToHigh,
    printSortedGames,
    sort_with_pandas,
    get_sorting_method,
)
from gameSearchFunctions import find_game_by_name, print_matching_games, navprompt
from insightsreport import (
    gameage_retention_findings,
    least_played_game_value_print,
    print_least_played,
    most_played_game,
    print_most_played,
    gameage_playercount_correlation,
    most_popular_genre,
)
from genreSearch import search_games_by_genre

# ascii text art library used to help improvee text UI
from pyfiglet import Figlet

# declare the dataset which is used for the program in variable for reuse
dataset = "games.csv"
totalrows = 0
totalColumns = 0
rowslist = []
# the main pyfiglet font which is used for the text interface
pygletfont = "slant"


fig = Figlet(font=pygletfont)
ascii_art5 = fig.renderText("Welcome to GameFinder")
print(ascii_art5)
# declares the initial function choice variable which represents where the user wants go go in the app - later updated with navprompt function
functionchoice = int(
    input(
        "1 - for game finder 2 - for genre search 3 - Search Game by Rating 4 -Review Findings:  "
    )
)


# this while loop contains the application in an active state until user enters 0 to exit the program
while functionchoice != 0:
    # Opens the dataset to 'read' and save the open stat in variable gamedata
    with open(dataset, "r") as gamedata:
        # Make a csv reader object
        csv_reader = csv.reader(gamedata)

        # Iterates through the rows of data
        for rows in csv_reader:
            # Takes the length of the row, which is the number of items in the list representing the row
            totalColumns = len(rows)
            # Adds one to the total row count for each repetition of the loop representing the number of rows of data in the dataset
            totalrows = totalrows + 1
            rowslist.append(rows)
        # game search funtionality - functions found in gamesearchfunctions.py
        if functionchoice == 1:
            gametofind = input("What is the name of the game you want to find?")
            matching_games = find_game_by_name(csv_reader, gamedata, gametofind)
            # renders pyfiglet art
            resultArt = fig.renderText("Matching Games")
            print(resultArt)
            print_matching_games(matching_games)
            # navprompt function is the fucntion to handle navigation updates
            functionchoice = navprompt()
        # Search by genere functionality methods in
        elif functionchoice == 2:
            # found in gamesearch module, returns games that match genre
            search_games_by_genre(csv_reader, gamedata, pygletfont)
            functionchoice = navprompt()
            # handles the functions for listing games in order of rating
        elif functionchoice == 3:
            gamedata.seek(0)
            unsortedDict = getGamesWithRating(csv_reader)
            ordersort = int(input("1 - High to Low 2 - Low to high "))
            # order sort handles userinput to havigate within functionchoise 3 1 = high to low 2 = low to high
            if ordersort == 1:
                # sort method and get sort methdod used for choosing between padas approach or manual list approach
                # sort method 1 = dict sort method 2 = pandas approach
                sortMethod = get_sorting_method()
                while sortMethod != 0:
                    if sortMethod == 1:
                        sortedDict = sortDictHighToLow(unsortedDict)
                        printSortedGames(sortedDict, order=1)
                        sortMethod = get_sorting_method()
                    elif sortMethod == 2:
                        sort_with_pandas(False)
                        sortMethod = get_sorting_method()
                functionchoice = navprompt()
            elif ordersort == 2:
                sortMethod = get_sorting_method()
                while sortMethod != 0:
                    if sortMethod == 1:
                        sortedDict = sortDictLowToHigh(unsortedDict)
                        printSortedGames(sortedDict, order=2)
                        sortMethod = get_sorting_method()
                    elif sortMethod == 2:
                        sort_with_pandas(True)
                        sortMethod = get_sorting_method()

                functionchoice = navprompt()
                # function choice 4 returns a report on genreal data findings
        elif functionchoice == 4:
            findingsAscii = fig.renderText("Findings From Data")
            gameage_retention_findings()
            gameage_playercount_correlation()
            least_played_game_value_print()
            print_least_played()
            most_played_game()
            print_most_played()
            most_popular_genre()
            functionchoice = navprompt()
        # handels input error in navigation
        else:
            print("Invalid Choose a value indicated")
            functionchoice = navprompt()
    print("current function choice", functionchoice)
endfig = Figlet(font=pygletfont)
leaveMessage = endfig.renderText("Program Ending, GoodBye Sunshine")
print(leaveMessage)


# pritns rows and columns total to confirm dataset has laoded correctly
print(f"This dataset has {totalrows} rows and {totalColumns} columns of data per row")

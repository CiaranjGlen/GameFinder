import pandas as pd


def getGamesWithRating(csv_reader):
    games_dict = {}
    for row in csv_reader:
        if row[4] != "":
            game_name = row[1]
            rating = row[4]
            games_dict[game_name] = rating
    return games_dict


def sortDictHighToLow(unsortedDict):
    return sorted(unsortedDict.items(), key=lambda item: item[1], reverse=True)


def sortDictLowToHigh(unsortedDict):
    return sorted(unsortedDict.items(), key=lambda item: item[1])


def printSortedGames(sortedDict, order):
    furtherReturns = True
    sliceincrementhigh = 10
    sliceincrementlow = 0
    if order == 1:
        print("Here are the highest rated games:")
    elif order == 2:
        print("Here are the lowest rated games:")
    while furtherReturns:
        games_to_display = sortedDict[sliceincrementlow:sliceincrementhigh]

        for game, rating in games_to_display:
            print(f"{game}: {rating}")

        sliceincrementlow = sliceincrementhigh
        sliceincrementhigh += 10
        furtherReturns = input("1 return next 10 2 - Go back") == "1"


def sort_with_pandas(sortingOrder):
    df = pd.read_csv("games.csv")
    df = df.sort_values(by="Rating", ascending=sortingOrder)
    further_returns = True
    slice_increment_low = 0
    slice_increment_high = 10

    while further_returns:
        # Print the next 10 games for the current slice
        print(df.iloc[slice_increment_low:slice_increment_high][["Title", "Rating"]])

        slice_increment_low += 10
        slice_increment_high += 10
        further_returns = input("1 - return next 10, 2 - Go back: ") == "1"


def get_sorting_method():
    methodvalue = int(input("1 - View List return 2- View Panda Return 0 - Go Back"))
    return methodvalue

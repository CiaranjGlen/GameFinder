import pandas as pd
from datetime import datetime
from pyfiglet import Figlet


# pre process the csv read and clean data to usable format
def fixed_csv():
    df = pd.read_csv("games.csv")
    df = df.dropna(subset=["Playing"])
    df["Playing"] = df["Playing"].apply(convert_to_numeric)
    df["Plays"] = df["Plays"].apply(convert_to_numeric)
    df["Release Date"] = pd.to_datetime(
        df["Release Date"], format="%b %d, %Y", errors="coerce"
    )
    # Filter out rows with NaT values
    df = df.dropna(subset=["Release Date"])
    return df


def convert_to_numeric(value):
    if "K" in value:
        return float(value.replace("K", "")) * 1e3
    elif "M" in value:
        return float(value.replace("M", "")) * 1e6
    else:
        return pd.to_numeric(value, errors="coerce")


# age and player basse retention functions
def gameage_retention_findings():
    df = fixed_csv()

    current_date = datetime.now()
    df["Game Age (days)"] = (current_date - df["Release Date"]).dt.days
    df["Plays - Playing"] = df["Plays"] - df["Playing"]
    correlation = df["Game Age (days)"].corr(df["Plays - Playing"])
    heading = Figlet(font="bubble")
    headingPrint = heading.renderText("Correlation Findings:")
    print(headingPrint)
    # Display the correlation information
    print(
        f"""
    The correlation coefficient between the age of a game and player retention is approximately {correlation:.2f}.
    This positive correlation of 0.08 suggests a slight tendency for older games to have higher player retention rates.
    While correlation provides insight, it's essential to note that correlation does not imply causation.
    This value helps us understand the relationship between these variables./n
    """
    )


def gameage_playercount_correlation():
    df = fixed_csv()
    current_date = datetime.now()
    df["Game Age (days)"] = (current_date - df["Release Date"]).dt.days

    correlation = df["Game Age (days)"].corr(df["Playing"])
    heading = Figlet(font="bubble")
    headingPrint = heading.renderText("Correlation Findings:")
    print(headingPrint)
    # Display the correlation information
    print(
        f"""
    The correlation coefficient between the age of a game and player count is approximately {correlation:.2f}.
    This very weak positive correlation of {correlation:.2f} suggests a slight tendency for older games to have a slightly higher player count.
    
    """
    )


# most and least active game functions


def least_played_game_value_print():
    df = fixed_csv()
    minIndex = df["Playing"].idxmin()
    leastPlayedGame = df.loc[minIndex]
    heading = Figlet(font="bubble")
    headingPrint = heading.renderText("Least Played Game Data")
    print(headingPrint)
    print(
        f"The least played games in the the database has {leastPlayedGame['Playing']} active players: "
    )


def least_played_game_value_assign():
    df = fixed_csv()
    minIndex = df["Playing"].idxmin()
    leastPlayedGame = df.loc[minIndex]
    return leastPlayedGame


leastPlayedValue = least_played_game_value_assign()


def print_least_played():
    df = fixed_csv()

    # Print table headers
    print(f"{'Title':<40}{'Playing':<10}")

    # Iterate through DataFrame rows and print inactive games as a table
    for index, row in df.iterrows():
        if row["Playing"] == leastPlayedValue["Playing"]:
            print(f"{row['Title']:<40}{int(row['Playing']):<10}")


def most_played_game():
    df = fixed_csv()
    maxIndex = df["Playing"].idxmax()
    mostPlayedGame = df.loc[maxIndex]
    print(
        f"The most played games in the database have  {mostPlayedGame['Playing']} active players :"
    )


def most_played_value_assign():
    df = fixed_csv()
    maxIndex = df["Playing"].idxmax()
    mostPlayedGame = df.loc[maxIndex]
    mostPlayedCount = mostPlayedGame["Playing"]
    return mostPlayedCount


mostPlayedPlayercount = most_played_value_assign()


def print_most_played():
    df = fixed_csv()
    printed_titles = set()

    for index, row in df.iterrows():
        if (
            int(row["Playing"]) == mostPlayedPlayercount
            and row["Title"] not in printed_titles
        ):
            print(f"{row['Title']:<30}{int(row['Playing']):<10}")
            printed_titles.add(row["Title"])


# finds and prints the most popular game genre  from the dataset
def most_popular_genre():
    df = fixed_csv()

    # Convert the 'Genres' column to a list type
    df["Genres"] = df["Genres"].apply(eval)

    # Use explode to separate genres from list form to own row
    df_exploded = df.explode("Genres").reset_index(drop=True)

    # Group by genre and calculate the sum of players
    genre_player_sum = df_exploded.groupby("Genres")["Playing"].sum()

    most_players_genre = genre_player_sum.idxmax()

    print(f"The genre with the most players is: {most_players_genre}")
    print(
        f"here is a list of genres and theie player count {genre_player_sum.sort_values(ascending=False)}/n"
    )

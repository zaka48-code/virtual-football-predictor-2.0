import pandas as pd

def load_teams(file_path="data/teams.csv"):
    """
    Charge la liste des équipes depuis le CSV.
    Retourne une liste de noms d'équipes.
    """
    df = pd.read_csv(file_path)
    return df["team_name"].tolist()

def load_leagues(file_path="data/leagues.csv"):
    """
    Charge la liste des ligues depuis le CSV.
    Retourne une liste de noms de ligues.
    """
    df = pd.read_csv(file_path)
    return df["league_name"].tolist()

def load_matches(file_path="data/matches.csv", league=None):
    """
    Charge les matchs depuis le CSV.
    Si league est fourni, filtre par ligue.
    Retourne un DataFrame pandas.
    """
    df = pd.read_csv(file_path)
    if league:
        df = df[df["league"] == league]
    return df

def last_n_matches(df_matches, team, n=20):
    """
    Retourne les derniers n matchs d'une équipe dans le DataFrame.
    """
    team_matches = df_matches[(df_matches["team1"] == team) | (df_matches["team2"] == team)]
    return team_matches.tail(n)

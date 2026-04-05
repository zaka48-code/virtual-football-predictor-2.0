import pandas as pd

def analyze_team(team, results_text, ranking_text, matches_csv, league):
    """
    Analyse la forme récente sur 20 derniers matchs
    """
    df_matches = pd.read_csv(matches_csv)
    df_league = df_matches[df_matches["league"]==league]

    # Filtrer derniers matchs de l'équipe
    team_matches = df_league[(df_league["team1"]==team) | (df_league["team2"]==team)]
    last_matches = team_matches.tail(20)

    wins = 0
    draws = 0
    losses = 0
    goals_for = 0
    goals_against = 0

    for _, row in last_matches.iterrows():
        score1, score2 = map(int, row["score"].split("-"))
        if row["team1"] == team:
            gf, ga = score1, score2
        else:
            gf, ga = score2, score1

        goals_for += gf
        goals_against += ga

        if gf > ga:
            wins +=1
        elif gf == ga:
            draws +=1
        else:
            losses +=1

    stats = {
        "team": team,
        "league": league,
        "wins": wins,
        "draws": draws,
        "losses": losses,
        "goals_for": goals_for,
        "goals_against": goals_against
    }
    return stats

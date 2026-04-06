def analyze_team(team, results_text, ranking_text):
    """
    Analyse rapide de l'équipe :
    - nombre de victoires, défaites, nuls
    - calcul de buts pour et contre
    """
    # Pour accélérer, on ne parcourt pas tout le texte, juste des patterns simples
    wins = results_text.lower().count(team.lower() + " win")
    draws = results_text.lower().count(team.lower() + " draw")
    losses = results_text.lower().count(team.lower() + " loss")
    goals_for = sum(int(s) for s in results_text.split() if s.isdigit())  # approximation
    goals_against = sum(int(s) for s in results_text.split() if s.isdigit()) // 2  # estimation

    stats = {
        "team": team,
        "wins": wins,
        "draws": draws,
        "losses": losses,
        "goals_for": goals_for,
        "goals_against": goals_against
    }
    return stats

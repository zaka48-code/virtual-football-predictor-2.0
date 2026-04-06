def predict_match(stats, pattern):
    """
    Prédiction basée sur la forme récente et le pattern détecté
    """
    score = stats["wins"]*3 + stats["draws"]
    if pattern == "Cycle détecté":
        score += 2  # bonus si cycle détecté

    if score >= 10:
        return "Victoire très probable"
    elif score >= 6:
        return "Match équilibré"
    else:
        return "Défaite possible"

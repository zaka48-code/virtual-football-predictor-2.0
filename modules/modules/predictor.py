def predict_match(stats, pattern):
    score = stats["wins"]*3 + stats["draws"]
    if pattern == "Cycle détecté":
        score += 2

    if score >= 15:
        prediction = "Victoire très probable"
        probability = 85
    elif score >= 10:
        prediction = "Victoire probable"
        probability = 70
    elif score >= 6:
        prediction = "Match équilibré"
        probability = 50
    else:
        prediction = "Défaite possible"
        probability = 30

    return prediction, probability

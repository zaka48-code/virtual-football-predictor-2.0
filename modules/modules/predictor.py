def detect_pattern(results_text):
    results_list = []
    for line in results_text.splitlines():
        if "win" in line.lower():
            results_list.append("W")
        elif "draw" in line.lower():
            results_list.append("D")
        elif "loss" in line.lower():
            results_list.append("L")

    if len(results_list) < 8:
        return "Pas assez de données"

    if results_list[-4:] == results_list[-8:-4]:
        return "Cycle détecté"

    return "Aucun cycle"

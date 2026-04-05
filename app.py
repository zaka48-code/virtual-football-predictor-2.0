import streamlit as st
import pandas as pd
from modules.ocr_reader import read_image
from modules.team_analyzer import analyze_team
from modules.predictor import predict_match
from modules.pattern_detector import detect_pattern

st.title("Virtual Football AI Predictor")

# Charger équipes et ligues
teams = pd.read_csv("data/teams.csv")["team_name"].tolist()
leagues = pd.read_csv("data/leagues.csv")["league_name"].tolist()

# Menus déroulants
team = st.selectbox("Choisir l'équipe cible", teams)
league = st.selectbox("Choisir la ligue", leagues)

# Upload captures
results_img = st.file_uploader("Résultats récents", type=["png","jpg","jpeg"])
ranking_img = st.file_uploader("Classement", type=["png","jpg","jpeg"])
next_match_img = st.file_uploader("Prochains matchs", type=["png","jpg","jpeg"])

if st.button("Analyser"):
    st.write("Analyse en cours...")

    # Lire texte des images
    results_text = read_image(results_img)
    ranking_text = read_image(ranking_img)
    next_match_text = read_image(next_match_img)

    # Analyse de l'équipe
    stats = analyze_team(team, results_text, ranking_text, matches_csv="data/matches.csv", league=league)

    # Détection de cycles
    pattern = detect_pattern(results_text)

    # Prédiction
    prediction, probability = predict_match(stats, pattern)

    # Affichage
    st.subheader("Texte extrait des images :")
    st.text("Résultats récents :\n" + results_text)
    st.text("Classement :\n" + ranking_text)
    st.text("Prochains matchs :\n" + next_match_text)

    st.subheader("Analyse")
    st.json(stats)
    st.write("Cycle détecté :", pattern)

    st.subheader("PRÉDICTION")
    st.success(f"{prediction} (Probabilité : {probability}%)")

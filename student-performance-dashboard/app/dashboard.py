import streamlit as st
import pandas as pd
from .data_processing import preprocess_data
from .feature_selection import select_important_features
import plotly.express as px

@st.cache_resource
def load_data():
    return pd.read_csv('data/students_data.csv')

def get_encoded_column_name(df_encoded, original_name):
    for column in df_encoded.columns:
        if original_name in column:
            return column
    return original_name

def run_dashboard():
    df = load_data()
    top_features = select_important_features(df)
    
    # Filtrer le DataFrame pour ne conserver que les colonnes de type int64
    numeric_features = df.select_dtypes(include=['int64']).columns.tolist()
    
    # Lister toutes les colonnes sauf les colonnes non pertinentes
    excluded_features = ["FinalGrade", "StudentID", "age", "schoolsup_yes"]
    all_possible_features = [col for col in numeric_features if col not in excluded_features]
    
    # Retirer les fonctionnalités déjà importantes de la liste des fonctionnalités possibles
    selectable_features = list(set(all_possible_features) - set(top_features))

    # Multi-sélection Streamlit
    st.sidebar.title('Variables supplémentaires')
    additional_features = st.sidebar.multiselect(
        "Sélectionnez des fonctionnalités supplémentaires", selectable_features)
    
    # Combiner les fonctionnalités sélectionnées par le modèle et celles choisies par l'expert
    all_selected_features = [f for f in (top_features + additional_features) if f not in excluded_features]

    st.sidebar.title('Pondérations des facteurs explicatifs')
    weights = {}
    for feature in all_selected_features:
        weight = st.sidebar.slider(feature, 0.0, 3.0, 1.0)
        weights[feature] = weight
        
    df_encoded = preprocess_data(df)
    df_encoded["Performance"] = df_encoded["FinalGrade"]
    df_encoded["Complexity"] = sum(df_encoded[get_encoded_column_name(df_encoded, feature)] * weight for feature, weight in weights.items())
    
    # Visualisez les résultats
    st.title("Performance des élèves vs. Complexité d'accompagnement")
    st.plotly_chart(
        px.scatter(df_encoded, x="Performance", y="Complexity", hover_data=["StudentID", "age"], 
                   title="Performance vs. Complexité d'accompagnement")
    )

import pandas as pd

categorical_features = ['school', 'sex', 'address', 'famsize', 'Pstatus', 'Mjob', 'Fjob', 
                        'reason', 'guardian', 'schoolsup', 'famsup', 'paid', 'activities', 
                        'nursery', 'higher', 'internet', 'romantic']

def preprocess_data(df):
    
    # Suppression des colonnes non pertinentes
    df = df.drop(columns=['FirstName', 'FamilyName'], errors='ignore')
    
    # 1. Vérification du format des colonnes
    for col in categorical_features:
        if col not in df.columns:
            raise ValueError(f"La colonne {col} est manquante dans le DataFrame fourni.")
        
        if not pd.api.types.is_categorical_dtype(df[col]) and not pd.api.types.is_object_dtype(df[col]):
            raise TypeError(f"La colonne {col} devrait être de type catégoriel ou objet, mais elle est de type {df[col].dtype}.")

    # 2. Nettoyage des valeurs indésirables
    # Supprimer les lignes avec des valeurs NaN (vous pouvez également les imputer si nécessaire)
    df = df.dropna(subset=categorical_features)
    
    # Autres nettoyages si nécessaires...
    
    # Encodage One-Hot des colonnes catégorielles
    df_encoded = pd.get_dummies(df, columns=categorical_features, drop_first=True)

    
    return df_encoded

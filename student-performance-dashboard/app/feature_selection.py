import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from .data_processing import preprocess_data  # Importation de preprocess_data

def select_important_features(df, n_top_features=5):
    df_encoded = preprocess_data(df)
    X = df_encoded.drop("FinalGrade", axis=1)
    print(X.dtypes)
    y = df_encoded["FinalGrade"]
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    feature_importances = model.feature_importances_
    important_features = pd.Series(feature_importances, index=X.columns).sort_values(ascending=False)
    
    return important_features.index[:n_top_features].tolist()

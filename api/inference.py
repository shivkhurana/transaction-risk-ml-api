import joblib
import pandas as pd

# Load into memory once when server starts
try:
    model = joblib.load('ml_pipeline/saved_models/risk_classifier.pkl')
except FileNotFoundError:
    model = None

def evaluate_risk(amount: float, user_age_days: int) -> str:
    if not model:
        return "Model not loaded"
        
    features = pd.DataFrame([[amount, user_age_days]], columns=['amount', 'user_age_days'])
    prediction = model.predict(features)
    
    # Isolation forest returns -1 for anomalies, 1 for normal
    return "High Risk (Anomaly)" if prediction[0] == -1 else "Low Risk"
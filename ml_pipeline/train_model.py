import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest

def train_anomaly_detector():
    print("Loading transaction data...")
    # Dummy data generation for the prototype
    data = pd.DataFrame({
        'amount': [10.5, 20.1, 15.0, 10000.5, 12.0], # 10000.5 is the anomaly
        'user_age_days': [300, 450, 200, 2, 500]
    })
    
    print("Training Isolation Forest model...")
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(data)
    
    # Save the model weights for the API to use
    joblib.dump(model, 'saved_models/risk_classifier.pkl')
    print("Model saved to saved_models/risk_classifier.pkl")

if __name__ == "__main__":
    train_anomaly_detector()
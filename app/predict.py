import joblib
import pandas as pd

model = joblib.load("model.joblib")
feature_order = joblib.load("feature_order.joblib")

def predict(features_dict):
    """
    features_dict: dictionary {feature_name: value}
    returns: 0 or 1
    """
    # keep the input order identical to training
    values = [features_dict[f] for f in feature_order]
    X = pd.DataFrame([values], columns=feature_order)
    return model.predict(X)[0]

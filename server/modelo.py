import json
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
modelo = joblib.load('modelo.pkl')
scaler = joblib.load('scaler.pkl')
def predict_fraud(data):  
    # data_json = json.loads(json.dumps(data))
    data = pd.DataFrame([data])
    print(data.info())
    data = scaler.transform(data)
    prediction = modelo.predict(data)
    return 'Fraude' if prediction[0] == 1 else 'No fraude'
    
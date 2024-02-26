import requests
URL_API = 'https://api.ejemplo.com/data'


# option with API 
# def predict(data):
#     response = requests.post(URL_API, json=data)
#     prediction = response.json()
#     return prediction

# test :v
def predict(data):
    return "Fraude"

# option local model
# def predict(data):
#     # Load the model
#     model = joblib.load("model.joblib")

#     # Make a prediction
#     prediction = model.predict(data)

#     return prediction

import requests
URL_API = 'http://127.0.0.1:8000/predict/'


# option with API 
def predict(data):
    response = requests.post(URL_API, json=data)
    prediction = response.json()
    print(prediction)
    return prediction


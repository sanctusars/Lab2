from flask import Flask, request
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

NBU_API_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

def get_nbu_rate(date_str):
    params = {
        'valcode': 'USD',
        'date': date_str,
        'json': ''
    }
    try:
        response = requests.get(NBU_API_URL, params=params)
        data = response.json()
        if data:
            return f"USD rate on {date_str}: {data[0]['rate']} UAH"
        return "Data not found"
    except Exception as e:
        return f"Error accessing the NBU API: {e}"

@app.route("/currency")
def currency():
    if 'today' in request.args:
        target_date = datetime.now().strftime("%Y%m%d")
    elif 'yesterday' in request.args:
        target_date = (datetime.now() - timedelta(days=1)).strftime("%Y%m%d")
    else:
        return "Use ?today or ?yesterday parameter", 400

    return get_nbu_rate(target_date)

if __name__ == '__main__':
    app.run(port=8000)
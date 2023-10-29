import requests


# PNR_API_ENDPOINT = "https://pnr-status-indian-railway.p.rapidapi.com/pnr-check/"

headers = {
    "X-RapidAPI-Key": "7793b4719dmshf83c27e4462670ap120c0ejsn5a879cc4ff3b",
    "X-RapidAPI-Host": "pnr-status-indian-railway.p.rapidapi.com"
}





from flask import Flask, render_template, request,url_for,session,redirect
import requests

app = Flask(__name__)


app.secret_key = "super secret key"
# RAPIDAPI_KEY = "c"
BASE_PNR_API_ENDPOINT = "https://pnr-status-indian-railway.p.rapidapi.com/pnr-check/{}"



@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""

    if request.method == 'POST':
        pnr = request.form['pnr']
        result = check_pnr(pnr)

    return render_template('result.html', result=result)


def check_pnr(pnr):
    api_endpoint = BASE_PNR_API_ENDPOINT.format(pnr)

    try:
        response = requests.get(api_endpoint, headers=headers)
        response.raise_for_status()
        data = response.json()

        if data.get('code') == 200:
            return data.get('data')
        else:
            result = f"PNR - {pnr} not found or invalid"
            return result
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(port=int("3001"),host="0.0.0.0")

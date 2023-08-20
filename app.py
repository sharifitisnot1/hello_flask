from flask import Flask, render_template, request
from googleapiclient.discovery import build
import requests

API_KEY_YOUTUBE = 'APPIKEY123456789'
API_KEY_ALPHAVANTAGE = 'APIKEYABCDEFGHIJK'

youtube = build('youtube', 'v3', developerKey=API_KEY_YOUTUBE)
app = Flask(__name__)

BASE_URL_ALPHAVANTAGE = 'https://www.alphavantage.co/query'

def search_videos_by_category(category, max_results=5):
    search_response = youtube.search().list(
        q=category,
        type='video',
        part='id,snippet',
        maxResults=max_results
    ).execute()

    videos = []
    for item in search_response['items']:
        video = {
            "title": item['snippet']['title'],
            "description": item['snippet']['description'],
            "videoId": item['id']['videoId']
        }
        videos.append(video)

    return videos

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search_by_category():
    category = request.form.get("category")
    if category:
        videos = search_videos_by_category(category)
        return render_template("results.html", category=category, videos=videos)
    else:
        return "No category provided."

@app.route('/get_stock_quote', methods=['GET'])
def get_stock_quote():
    symbol = request.args.get('symbol')

    if symbol:
        params = {
            'function': 'GLOBAL_QUOTE',
            'symbol': symbol,
            'apikey': API_KEY_ALPHAVANTAGE
        }

        response = requests.get(BASE_URL_ALPHAVANTAGE, params=params)
        data = response.json()

        if 'Global Quote' in data:
            quote = data['Global Quote']
            return render_template('index.html', quote=quote, symbol=symbol)
        else:
            error_message = "No data available for the symbol."
            return render_template('index.html', error=error_message, symbol=symbol)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

    

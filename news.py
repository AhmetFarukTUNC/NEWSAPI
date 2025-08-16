from flask import Flask, jsonify, send_file, request
import requests

app = Flask(__name__)

API_KEY = "<YOU CAN API KEY HERE THAT TOOK FROM NEWSAPİ WEBSİTE>"
EVERYTHING_URL = "https://newsapi.org/v2/everything"

@app.route("/")
def home():
    return send_file("index.html")  # templates yok

@app.route("/api/haberler")
def haberler():
    query = request.args.get("q", "futbol")  # default 'futbol'
    try:
        response = requests.get(EVERYTHING_URL, params={
            "apiKey": API_KEY,
            "q": query,
            "language": "tr",
            "sortBy": "publishedAt"
        })
        data = response.json()
        return jsonify(data.get("articles", []))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

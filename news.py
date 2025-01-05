import requests


everything_url = "https://newsapi.org/v2/everything"

api_key = "<You must your api key.>"




response2 = requests.get(everything_url, params={
    "apiKey": api_key,
    "q": "futbol",
    "language": "tr",
    "sortBy": "publishedAt"
})




haberler2 = response2.json()["articles"]

for i in haberler2:
     print(i["source"]["name"])
     print(i["title"])
     print(i["url"])
     print("-------------------------------------------------------------")

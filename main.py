import requests
import json

query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-04-09&sortBy=publishedAt&apiKey=39a373fcc1a445049123db17acde62ff"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))

for article in news["articles"]:
  print(article["title"])
  print(article["description"])
  print("--------------------------------------")
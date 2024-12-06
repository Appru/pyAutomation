import requests
import sys

# r = requests.get("https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2024-11-14&to=2024-12-02&sortBy=popularity&language=en&apiKey=2a15a7a664274229b27854782c2780b8")
# content = r.json()
# print (type(content))

#  print(content["articles"][0]["title"])
#  print(content["articles"][0]["description"])
#  print(content["articles"][0]["publishedAt"])

# articles = content["articles"]

# for article in articles:
#     print('TITLE:\n', article["title"], '\nDESCRIPTION\n', article["description"], '\nDATE\n',article["publishedAt"])




def get_news(country, api_key='2a15a7a664274229b27854782c2780b8'):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content["articles"]
    results = []
    

    for article in articles:
         results.append(f"TITLE\n'{article['title']}, '\nDESCRIPTION\n', {article['description']}")


    return results

print(get_news(country="us"))
#print(sys.version)
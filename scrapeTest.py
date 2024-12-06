import requests


def getData(city):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&APPID=d1dad410ac64a8e7005ac65f2d6e8277&units=metric'
    r = requests.get(url)
    content = r.json()
    with open('data.txt', 'a') as file:
        for dicty in content['list']:
            file.write(f"{city},{dicty['dt_txt']},{dicty['dt_txt']}, {dicty['main']['temp']}, {dicty['weather'][0]['description']}\n")



    


print(getData(city="london"))
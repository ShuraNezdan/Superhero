import requests

name_hero = ['Hulk', 'Captain America', 'Thanos', 'Iron Man']
intelligence = {}

HOST = 'https://superheroapi.com/api/2619421814940190/'
# HEADERS = {'Content-Type': 'application/json', 'Authorization': 'OAuth 2619421814940190'}


# Считываем данные с сайта в формате json через имя в name_hero
def hero(host, hero):
    url = f'{host}search/{hero}'
    response = requests.get(url)
    # создаем словарь - имя: "ум"
    intelligence[response.json()['results'][0]['name']] = int(response.json()['results'][0]['powerstats']['intelligence'])
    return intelligence


# Находим самого умного через max()
def max_intelligence():
    for name in name_hero:
        hero(HOST, name)
    print(intelligence)
    max_intelligence_value = max(intelligence.values())
    w = [key for key, value in intelligence.items() if value == max_intelligence_value]

    print(f'Самые умные супергерои, это - {w}')

 
    


if __name__ == '__main__':
    max_intelligence()
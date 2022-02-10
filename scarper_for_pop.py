
import enum
from bs4 import BeautifulSoup
import requests
import random


def scrape_top(num):
    IMDB = 'https://www.imdb.com'
    CHART = IMDB + '/chart/moviemeter/'
    r = requests.get(CHART)

    soup = BeautifulSoup(r.content, 'html5lib')

    movies = []

    ratings = [ir['data-value']
               for ir in soup.select('td.posterColumn span[name=ir]', limit=num)]

    velocity = soup.select('span [class=velocity]', limit=num)

    for i, rating in enumerate(ratings):
        movie = {}
        up_or_down = random.randint(0, 1)
        climb = random.randint(0, 5)
        movie = {
            'rating': rating,
            'up_or_down': up_or_down,
            'climb': climb,
            'rank': i+1
        }
        movies.append(movie)

    for velo in velocity:
        up_or_down = 0
        if velo.find('span', class_='global-sprite titlemeter up'):
            up_or_down = 1
        # velo_text = velo.text
        # velo_text.replace('\\n', '')
        # velo_text.replace('(', '')
        # velo_text.replace(')', '')
        print(up_or_down)
        # climb = velo_text.split()[1]
        # movie = {
        #     'up_or_down': up_or_down,
        #     'climb': climb
        # }
        # movies.append(movie)
    #    1\n(\n\n9)\n
    return movies


scrape_top(5)

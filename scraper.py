
from bs4 import BeautifulSoup
import filehandler as fh
import requests


def scrape_top(num):
    IMDB = 'https://www.imdb.com'
    CHART = IMDB + '/chart/top/'
    r = requests.get(CHART)

    soup = BeautifulSoup(r.content, 'html5lib')

    movies = []

    links = [IMDB + a.attrs.get('href')
             for a in soup.select('td.titleColumn a', limit=num)]
    ratings = [strong.text for strong in soup.select(
        'td.ratingColumn strong', limit=num)]
    titles = [a.text for a in soup.select('td.titleColumn a', limit=num)]
    votes = [nv.attrs.get('data-value')
             for nv in soup.select('td.posterColumn span[name=nv]', limit=num)]
    ranks = [rk.attrs.get('data-value')
             for rk in soup.select('td.posterColumn span[name=rk]', limit=num)]

    for i in range(num):
        data = {
            'link': links[i],
            'rating': float(ratings[i]),
            'title': titles[i],
            'votes': int(votes[i]),
            'rank': int(ranks[i])
        }
        movies.append(data)
    fh.write_file(movies, 'old_ranking_data')


def scrape_oscars(movies):
    for movie in movies:
        r = requests.get(movie['link'])
        soup = BeautifulSoup(r.content, 'html5lib')
        soup.select


scrape_top(20)

import math


def review_penalizer(movies):
    benchmark = max(movies, key=lambda x: x['votes'])['votes']
    for movie in movies:
        penalty = math.floor((benchmark - movie['votes'])/100000) * 0.1
        movie['rating'] -= penalty
    return movies


def oscar_calculator(movies):
    for movie in movies:
        oscars = movie['oscars']
        if oscars > 10:
            movie['rating'] += 1.5
        elif oscars > 5:
            movie['rating'] += 1.0
        elif oscars > 2:
            movie['rating'] += 0.5
        elif oscars > 0:
            movie['rating'] += 0.3
    return movies


def new_ranking(movies):
    new_ranking = sorted(movies, key=lambda x: x['rating'], reverse=True)
    for i, movie in enumerate(new_ranking):
        movie['rank'] = i + 1
    return new_ranking


def rating_adjuster(movies):
    movies = review_penalizer(movies)
    movies = oscar_calculator(movies)
    return new_ranking(movies)

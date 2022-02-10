import filehandler as fh
import scarper_for_pop as pop


def midweek_adjustment(movies):
    sorted(movies, key=lambda x: x['rating'])
    for movie in movies:
        climb_slope = -1
        if movie['up_or_down'] == 1:
            climb_slope = 1
        new_rank = round((movie['rank'] + climb_slope*movie['climb'])/2)
        movie['new_rank'] = new_rank

    fh.write_file(movies, 'pop_adjusted')


movies = pop.scrape_top(5)
midweek_adjustment(movies)

import filehandler as fh
import rating_adjuster as ra
import scraper as scr


def main():
    movies = scr.scrape_top(20)
    movies_with_oscars = scr.scrape_oscars(movies)
    fh.write_file(movies_with_oscars, 'old_ranking_data')

    adjusted_rating = ra.rating_adjuster(movies_with_oscars)
    fh.write_file(adjusted_rating, 'new_ranking_data')


if __name__ == '__main__':
    main()

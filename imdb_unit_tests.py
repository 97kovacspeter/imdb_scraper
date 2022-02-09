from unittest.mock import patch
import unittest
import rating_adjuster as ra
import scraper as scr


class TestReviewPenalizer(unittest.TestCase):

    def test_no_penalty(self):
        movies = [{'votes': 1, 'rating': 1}]
        self.assertAlmostEqual(ra.review_penalizer(movies), movies)

    def test_one_penalty(self):
        movies = [{'votes': 1, 'rating': 1}, {'votes': 100001, 'rating': 1}]
        movies = ra.review_penalizer(movies)
        self.assertAlmostEqual(movies[0]['rating'], 0.9)

    def test_six_penalty(self):
        movies = [{'votes': 1, 'rating': 1}, {'votes': 600001, 'rating': 1}]
        movies = ra.review_penalizer(movies)
        self.assertAlmostEqual(movies[0]['rating'], 0.4)

    def test_over_a_point_penalty(self):
        movies = [{'votes': 1, 'rating': 1}, {'votes': 1000001, 'rating': 1}]
        movies = ra.review_penalizer(movies)
        self.assertAlmostEqual(movies[0]['rating'], 0.0)


class TestOscarCalculator(unittest.TestCase):

    def test_zero_oscars(self):
        movies = [{'oscars': 0, 'rating': 1}]
        movies = ra.oscar_calculator(movies)
        self.assertAlmostEqual(movies[0]['rating'], 1)

    def test_one_oscar(self):
        movies = [{'oscars': 1, 'rating': 1}]
        movies = ra.oscar_calculator(movies)
        self.assertAlmostEqual(movies[0]['rating'], 1.3)

    def test_two_oscars(self):
        movies = [{'oscars': 2, 'rating': 1}]
        movies = ra.oscar_calculator(movies)
        self.assertAlmostEqual(movies[0]['rating'], 1.3)

    def test_three_oscars(self):
        movies = [{'oscars': 3, 'rating': 1}]
        movies = ra.oscar_calculator(movies)
        self.assertAlmostEqual(movies[0]['rating'], 1.5)

    def test_five_oscars(self):
        movies = [{'oscars': 5, 'rating': 1}]
        movies = ra.oscar_calculator(movies)
        self.assertAlmostEqual(movies[0]['rating'], 1.5)

    def test_ten_oscars(self):
        movies = [{'oscars': 10, 'rating': 1}]
        movies = ra.oscar_calculator(movies)
        self.assertAlmostEqual(movies[0]['rating'], 2)

    def test_eleven_oscars(self):
        movies = [{'oscars': 11, 'rating': 1}]
        movies = ra.oscar_calculator(movies)
        self.assertAlmostEqual(movies[0]['rating'], 2.5)


class TestNewRanking(unittest.TestCase):

    def test_no_change(self):
        movies = [{'rating': 1, 'rank': 1}]
        self.assertAlmostEqual(ra.new_ranking(movies), movies)

    def test_swapping_places(self):
        movies = [{'rating': 1, 'rank': 1}, {'rating': 2, 'rank': 2}]
        self.assertAlmostEqual(ra.new_ranking(movies)[0]['rating'], 2)
        self.assertAlmostEqual(ra.new_ranking(movies)[0]['rank'], 1)


class TestScraper(unittest.TestCase):

    def test_scraped_twenty(self):
        movies = scr.scrape_top(20)
        self.assertAlmostEqual(len(movies), 20)
        for movie in movies:
            self.assertIsNotNone(movie['link'])
            self.assertIsInstance(movie['link'], str)
            self.assertIsNotNone(movie['rating'])
            self.assertIsInstance(movie['rating'], float)
            self.assertIsNotNone(movie['title'])
            self.assertIsInstance(movie['title'], str)
            self.assertIsNotNone(movie['votes'])
            self.assertIsInstance(movie['votes'], int)
            self.assertIsNotNone(movie['rank'])
            self.assertIsInstance(movie['rank'], int)

    def test_added_oscars(self):
        movies = scr.scrape_top(20)
        movies = scr.scrape_oscars(movies)
        self.assertAlmostEqual(len(movies), 20)
        for movie in movies:
            self.assertIsNotNone(movie['link'])
            self.assertIsInstance(movie['link'], str)
            self.assertIsNotNone(movie['rating'])
            self.assertIsInstance(movie['rating'], float)
            self.assertIsNotNone(movie['title'])
            self.assertIsInstance(movie['title'], str)
            self.assertIsNotNone(movie['votes'])
            self.assertIsInstance(movie['votes'], int)
            self.assertIsNotNone(movie['rank'])
            self.assertIsInstance(movie['rank'], int)
            self.assertIsNotNone(movie['oscars'])
            self.assertIsInstance(movie['oscars'], int)


if __name__ == '__main__':
    unittest.main()

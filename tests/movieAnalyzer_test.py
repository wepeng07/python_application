from email import header
from operator import index
from webbrowser import get
from xml.sax.handler import property_interning_dict
import pytest
import sys, os
import pandas as pd
from pandas import testing as tm
from numpy import testing as tn
import numpy as np
sys.path.insert(1, os.getcwd())
from src.movieAnalyzer import get_movies_data, pd, get_movies_interval, get_rating_popularity_stats, get_actor_movies_release_year_range, get_actor_median_rating, get_directors_median_reviews

class TestMovieAnalyzer_test:
    def test_get_movies_interval_1(self):
        res = get_movies_interval(1992,1993)
        expected = pd.Series(["Schindler's List", 'Reservoir Dogs', 'Unforgiven', 'Jurassic Park', 'In the Name of the Father', 'Groundhog Day'])
        tm.assert_series_equal(expected, res, check_index=False, check_names=False,check_dtype=False)


    def test_get_movie_interval_2(self):
        
        with pytest.raises(ValueError, match='wrong input, y1 cannot bigger than y2'):
            get_movies_interval(1993,1992)
            # print('sjhfbhjabfjhaf', a)
            # assert "a" == "b"
            # raise ValueError('wrong input, y1 cannot bigger than y2'')
            # match='wrong input, y1 cannot bigger than y2'

       

    
    def test_get_rating_popularity_status_1(self):
        res = get_rating_popularity_stats('Popularity Index', 'mean')
        assert res == 1091.92

    def test_get_rating_popularity_status_2(self):
        res = get_rating_popularity_stats('Popularity Index','count')
        assert res == 207

    def test_get_rating_popularity_status_3(self):
        res = get_rating_popularity_stats('Popularity Index', 'median')
        assert res == 673.0

    def test_get_rating_popularity_status_4(self):
        res = get_rating_popularity_stats('Popularity Index', 'min')
        assert res == 3
        
    def test_get_rating_popularity_status_5(self):
        res = get_rating_popularity_stats('Popularity Index', 'max')
        assert res == 4940

    def test_get_rating_popularity_status_6(self):
        res = get_rating_popularity_stats('Rating', 'count')
        assert res == 207

    def test_get_rating_popularity_status_7(self):
        res = get_rating_popularity_stats('Rating', 'mean')
        assert res == 8.34
    
    def test_get_rating_popularity_status_8(self):
        res = get_rating_popularity_stats('Rating', 'median')
        assert res == 8.3
    
    def test_get_rating_popularity_status_9(self):
        res = get_rating_popularity_stats('Rating', 'min')
        assert res == 8.1

    def test_get_rating_popularity_status_10(self):
        res = get_rating_popularity_stats('Rating', 'max')
        assert res == 9.3

    def test_get_rating_popularity_status_11(self):
        with pytest.raises(ValueError,match=('input of type or index is wrong')):
            get_rating_popularity_stats('index', 'mean')
        
    def test_get_rating_popularity_status_12(self):
        with pytest.raises(ValueError,match=('input of type or index is wrong')):
            get_rating_popularity_stats('Popularity Index', '')

    def test_get_rating_popularity_status_13(self):
        with pytest.raises(ValueError,match=('input of type or index is wrong')):
            get_rating_popularity_stats('rating', 'mean')

    def test_get_rating_popularity_status_14(self):
        with pytest.raises(ValueError,match=('input of type or index is wrong')):
            get_rating_popularity_stats('', 'mean')

    def test_get_movie_release_year_range_1(self):
        res = get_actor_movies_release_year_range('Leonardo DiCaprio', 2022, 2010)
        expected = pd.Series([2010, 2012, 2013, 2010] , index=['Inception', 'Django Unchained', 'The Wolf of Wall Street','Shutter Island'])
        tm.assert_series_equal(expected, res, check_index=False, check_names=False)
    

    def test_get_movie_release_year_range_2(self):
        res = get_actor_movies_release_year_range('Leonardo DiCaprio', 1993, 1992)
        expected = pd.Series([],dtype='object')
        tm.assert_series_equal(expected, expected, check_index=False, check_names=False, check_dtype=False)

    def test_get_movie_release_year_range_3(self):
        with pytest.raises(ValueError,match='interval input is wrong'):
            get_actor_movies_release_year_range('Leonardo DiCaprio', 1992, 1993)

    def test_get_movie_release_year_range_4(self):
        with pytest.raises(TypeError,match='wrong input'):
            get_actor_movies_release_year_range('Leonardo DiCaprio', 'year', 'year')
        
    def test_get_actor_median_rating_1(self):
        res = get_actor_median_rating('Leonardo DiCaprio')
        assert res == 8.3

    def test_get_actor_median_rating_2(self):
        with pytest.raises(TypeError,match=('Wrong input')):
            get_actor_median_rating(2012)

    def test_get_actor_median_rating_3(self):
        with pytest.raises(ValueError,match=('the input is an empty string')):
            get_actor_median_rating('')

    def test_get_directors_median_reviews_1(self):
        res = get_directors_median_reviews()
        res_sum = res.sum()
        assert res_sum == 79.666
        res_max =res.max()
        assert res_max == 1.9500000000000002
        res_median =res.median()
        assert res_median == 0.566
        res_tail = res.iloc[-1]
        assert res_tail == 0.248
        res_head = res.iloc[0]
        assert res_head == 0.19



# get_movies_data()
# print(get_movies_interval(1992,1993))
# print(get_movies_interval(1993,1991))

# print(get_rating_popularity_stats('Popularity Index', 'mean'))
# print(get_rating_popularity_stats(1,mean))
# print(get_actor_movies_release_year_range('Leonardo DiCaprio', 1993, 1992))
# print(get_actor_movies_release_year_range('Leonardo DiCaprio', 2022, 2010))
# print(get_actor_median_rating(''))
# get_actor_median_rating('Tyrone Power')
# print(get_directors_median_reviews())




    #     dataframe_map = {
    #         "movie_name": ['A', 'B', 'C'],
    #         "release_year": ['1991', '1992', '1993'] 
    #     }
    #     df = pd.DataFrame(dataframe_map)
    #     print("DF: ", df)
    #     tm.assert_frame_equal(df, df)

    #     exp_values = [[1, 2, 0], [0, 1, 1]]
    #     np_array = np.array(exp_values)
    #     np_array2 = np.array([[1, 2, 0], [0, 1, 0]])
    #     print("adshjksgd", np_array)
    #     tn.assert_array_equal(np_array, np_array2)


 # dataframe_map = {
        #     "Title": ['Inception', 'Django Unchained', 'The Wolf of Wall Street','Shutter Island'],
        #     "Year of Release": ['2010', '2012', '2013', '2010'] 
        # }
        # expected = pd.DataFrame(dataframe_map)
        # print("DF: ", expected)
        # tm.assert_frame_equal(expected, res,check_index_type=False)
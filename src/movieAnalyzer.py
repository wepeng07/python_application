# Run this script from the repository's root.

from ast import If, Index
from audioop import add
from cgitb import reset
from dataclasses import replace
from email import header
import os
from pickle import NONE
from statistics import mean, median
from typing import final
from xml.sax.handler import property_interning_dict
import pandas as pd
top200_movies_file = os.path.join('src', 'data', 'Top_200_Movies.csv')

def get_movies_data():
    return pd.read_csv(top200_movies_file)

def get_movies_interval(y1, y2):

    if (y1>y2):
        print('here')
        raise ValueError('wrong input, y1 cannot bigger than y2')
    data = get_movies_data()
    interval = data[(data['Year of Release'] >= y1) & (data['Year of Release'] <= y2)]['Title']
    return interval
   

def get_rating_popularity_stats(index, type):
    if (index != "Rating") and (index != "Popularity Index"):
            raise ValueError('input of type or index is wrong')
    if (type == ''):
            raise ValueError('input of type or index is wrong')
    data = get_movies_data()
    
    if (type == 'count'):
        data_notnull =data.loc[data[index].notnull()]
        return data_notnull[index].count()
    
    if (type == 'mean'):
        temp = data.copy()
        final = temp.loc[temp[index].notnull()]
        if index == "Popularity Index":
            fin_data = final[index].str.replace(',','').astype(int)
        else:
            fin_data = final[index]
        return round(fin_data.mean(),2)

    if (type == 'median'):
        temp = data.copy()
        final=temp.loc[temp[index].notnull()]
        if index == "Popularity Index":
            fin_data = final[index].str.replace(',','')
        else:
            fin_data = final[index]
        return round(fin_data.median(),2)

    if (type =='min'):
        temp = data.copy()
        final=temp.loc[temp[index].notnull()]
        if index == "Popularity Index":
            fin_data = final[index].str.replace(',','').astype(int)
        else:
            fin_data = final[index]
        return round(fin_data.min(),2)
    
    if (type == 'max'):
        temp = data.copy()
        final=temp.loc[temp[index].notnull()]
        if index == "Popularity Index":
            fin_data = final[index].str.replace(',','').astype(int)
        else:
            fin_data = final[index]
        return round(fin_data.max(),2)


def get_actor_movies_release_year_range(actor, upper, lower=0):
    if (lower > upper):
            raise  ValueError('interval input is wrong')
    if ((not isinstance(upper, int)) and (not isinstance(lower, int))):
            raise TypeError('wrong input')
    data = get_movies_data()
    data=data[(data['Year of Release'] >= lower) & (data['Year of Release'] <= upper)]
    data = data[data['Movie Cast'].str.contains(actor)]
    if data.empty:
        return pd.Series(dtype='object')
    ans = data[['Title', 'Year of Release']]
    my_series = pd.Series(ans['Year of Release'].values.tolist(), index=ans['Title'])

    return my_series

def get_actor_median_rating(actor):
    if(not isinstance(actor, str)):
            raise TypeError('Wrong input')
    if (actor==""):
            raise ValueError('the input is an empty string')
    data = get_movies_data()
    rating_data = data[data['Movie Cast'].str.contains(actor)]['Rating']
    median=rating_data.median()
    return median

def get_directors_median_reviews():
    data = get_movies_data()
    data = data[['Number of Reviews','Director']]
    data_with_m = data[data['Number of Reviews'].str.contains('M')]
    data_with_m = data_with_m['Number of Reviews'].str.replace('M','').astype(float)
    data_with_k = data[data['Number of Reviews'].str.contains('K')]
    data_with_k = data_with_k['Number of Reviews'].str.replace('K','')
    data_with_k = data_with_k.astype(float)/1000
    af_change_data = data_with_m.add(data_with_k,fill_value=0)
    data['Number of Reviews']=af_change_data
    f_data=data.groupby("Director")['Number of Reviews'].agg('median')
    return f_data.squeeze()


    
    


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

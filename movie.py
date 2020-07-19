# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 11:57:39 2020

@author: DELL
"""

import pandas as pd
r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")
m_cols = ['movie_id', 'title']
movies = pd.read_csv('u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")
ratings = pd.merge(movies, ratings)
ratings.head()
movieRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
movieRatings.head()
starWarsRatings = movieRatings['Star Wars (1977)']
starWarsRatings.head()
similarMovies = movieRatings.corrwith(starWarsRatings) # pairwise correlation of Star Wars vector of user rating with every other movie
similarMovies = similarMovies.dropna() # Drop any results that have no data
df = pd.DataFrame(similarMovies) # Construct a new Dataframe of movies and their correlation score to Star Wars
df.head(10)
similarMovies.sort_values(ascending=False)
import numpy as np
movieStats = ratings.groupby('title').agg({'rating': [np.size, np.mean]})
movieStats.head()
popularMovies = movieStats['rating']['size'] >= 100 # Ignore movies rated by less than 100 people
movieStats[popularMovies].sort_values([('rating', 'mean')], ascending=False)[:15]
df = movieStats[popularMovies].join(pd.DataFrame(similarMovies, columns=['similarity']))
df.head()
df.sort_values(['similarity'], ascending=False)[:5]
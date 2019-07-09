#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: ??
@author: li
@file: data_analysis.py
@time: 2019-07-09 14:02
"""

import pandas as pd
pd.set_option('display.max_columns', None)


rate = pd.read_table('ml-1m/ratings.dat', sep='\t', names=['user', 'item', 'rating', 'timestamp'], header=None)
print(rate.head())

movie = pd.read_table('ml-1m/movies.dat', sep='::', names=['MovieID', 'Title', 'Genres'], header=None, engine='python')
print(movie.head())

users = pd.read_table('ml-1m/users.dat', sep='::', names=['UserID', 'Gender', 'Age', 'Occupation', 'Zip-code'], header=None, engine='python')
print(users.head())
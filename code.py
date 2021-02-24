# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 23:27:18 2020

@author: wheejoo
"""

import scipy as sp
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import surprise
from surprise import Reader, Dataset
from surprise.model_selection import cross_validate

file = pd.read_csv('C:/Users/wheejoo/Desktop/newdata_1.csv')

# name_list = []
# menu_list = []

# for i in file['id']:
#     name_list.append(i)
# # print(name_list)

# for j in file['menu']:
#     menu_list.append(j)

name_list = []
menu_set = set()

# for i in file['id']:
#     name_list.append(i)
# # print(name_list)

# for j in file['menu']:
#     menu_set.add(j)

for i in file['id']:
    name_list.append(i)
    for j in file['menu']:
        menu_set.add(j)
        
menu_list = list(menu_set)
# print(menu_list)

reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(file[['id', 'menu', 'score']], reader)
# print(data)

trainset = data.build_full_trainset()
option = {'name' : 'pearson'}
algo = surprise.KNNBasic(sim_options = option)
algo.fit(trainset)
print(cross_validate(algo, data)["test_mae"].mean())
print(cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True))


who = int(input("닉네임을 입력해주세요: "))
print("\n")

index = name_list.index(who)
print('user_index: ', index)
print("\n")

result = algo.get_neighbors(index, k=5)
print("당신의 취향과 유사한 사용자는?: ", result)
print("\n")

print("당신에게 추천드리는 음식 : ", "\n")

for r1 in result:
    max_rating = data.df[data.df["id"]==r1]["score"].max()
    menu_id = data.df[(data.df["score"]==max_rating)&(data.df["id"]==r1)]["menu"].values
    
    for menu_item in menu_id:
        print(menu_item)
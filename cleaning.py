# Testing some data cleaning cases here


import pandas as pd 
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("all_season_batting_card.csv")


data = data.drop(['match_name', 'link', 'commentary', 'shortText', 'fullName', 'runningScore', 'city'], axis=1)

le = LabelEncoder()
data['name'] = le.fit_transform(data['name'])

print(data['name'])




data['captain'] = data['captain'].apply(lambda x: 1 if x==True else 0)
data['isNotOut'] = data['isNotOut'].apply(lambda x: 1 if x==True else 0)

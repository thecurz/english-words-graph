import pandas as pd
from helpers.checkpath import check_path 

# Current Working Directory
CWD = check_path()

# No es formato json, es json-L (no tiene comas separando los objetos) asi que usamos lines = True
data = pd.read_json(CWD + r'\datasets\first_news.json', lines = True)
print(data)
'''
Structure:
-link
-headline *
-category
-short_description *
-authors
-date
'''
data = data.drop(['link', 'category', 'authors', 'date'], axis = 1)

print(data)


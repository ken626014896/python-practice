import pandas as pd


a=pd.read_json('mysite_alldata.json',orient='values',encoding='utf-8')
# print(a.head())
# print(a.describe())
#
# print(a.info())
print(type(a))
print(a)
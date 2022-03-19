# Import your libraries
import pandas as pd

#filter Tricks
oscar_nominees.query('id == "1" | year == "2000"')
oscar_nominees[oscar_nominees.id.isin(["1", "2"])]
oscar_nominees[(oscar_nominees['id'] == 1) | (oscar_nominees['id'] == 2)] 
oscar_nominees[oscar_nominees['id'].isin([2,3])]
oscar_nominees.query('nominee == "Abigail Breslin"').groupby('movie').size().reset_index()
oscar_nominees.groupby('nominee').size().reset_index().query('nominee == "Abigail Breslin"')

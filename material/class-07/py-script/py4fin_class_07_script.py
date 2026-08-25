# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 21:02:01 2021

@author: Habac
"""

#%%''' Applications '''

'''1.a'''
# imports pandas
import pandas as pd

# "reads" xlsx
gapminder = pd.read_excel('gapminder.xlsx')

# "reads" dta, stata format
pd.read_stata('gapminder.dta')

#%%
'''2.a'''
# first 10 observations
gapminder.head()

# last 10 observations
gapminder.tail()

#%%
'''3.a'''
# extracts columns
gapminder.columns

# extracts the column index of the continent column
gapminder.columns.get_loc('continent')

# extracts index
gapminder.index

# unique values of the continent variable
gapminder.continent.unique()

'''
Selecting variables (columns) from a DataFrame
'''
# way 1:
# selects the continent variable as a series
gapminder.continent

# way 2:
# selects the continent variable as a series
gapminder['continent']

# way 3:
# selects the continent variable as a series using loc (rows can be selected)
gapminder.loc[:,'continent']
# selects the continent variable as a series using iloc (rows can be selected)
gapminder.iloc[:,1]

# way 4:
# selects the continent and lifeExp variables using loc (rows can be selected)
gapminder.loc[:,['continent','lifeExp']]
# selects the continent and lifeExp variables using iloc (rows can be selected)
gapminder.iloc[:,[1,3]]

# way 5:
# selects the variables from continent up to pop (inclusive) using loc (rows can be selected)
gapminder.loc[:,'continent':'pop']
# selects the variables from continent up to pop (4) using iloc (rows can be selected)
gapminder.iloc[:,1:5]

# way 6:
# selects the continent and lifeExp variables (rows cannot be selected)
gapminder[['continent','lifeExp']]

'''
Selecting variables (columns) from a DataFrame
'''
# filters continent == "Americas"
gapminder[gapminder['continent'] == "Americas"]

# filters continent == "Americas" or filters continent == "Asia"
gapminder[(gapminder['continent'] == "Americas") | (gapminder['continent'] == "Asia")]

# filters (continent == "Americas" or filters continent == "Asia") and year == 2007
gapminder[((gapminder['continent'] == "Americas") | (gapminder['continent'] == "Asia")) & (gapminder['year'] == 2007)]

# filters continent == "Americas" or filters year == 2007
gapminder1 = gapminder[(gapminder['continent'] == "Americas") & (gapminder['year'] == 2007)]

#%%
'''4.a'''
# sorts the values in descending order and shows the first observation
gapminder1.sort_values(['gdpPercap'], ascending=False).head(1)

# sorts the values in ascending order and shows the last observation
gapminder1.sort_values(['gdpPercap'], ascending=False).tail(1)

#%%
'''5.a'''
# resets the index and "drops" it
gapminder1 = gapminder1.reset_index(drop=True)

# deletes/removes the continent and year variable (column) (axis=1)
gapminder1 = gapminder1.drop(['continent','year'], axis = 1)

# deletes/removes the row with index 0 and 1 (axis=0)
gapminder1.drop([0,1], axis=0)

# adds country as the index, does it in-place
gapminder1.set_index('country', inplace=True)

# deletes/removes the row whose index equals Ecuador
gapminder1.drop(['Ecuador'], axis=0)

#%%
'''6.a'''
# re-assigns to the column its original name but in lowercase
gapminder1.columns = [i.lower() for i in list(gapminder1.columns)]

# renames the column country to nation
gapminder.rename(columns={'country':'nation'})

#%%
'''7.a'''
# generates the variable lifeexp * 12 and assigns it to the DataFrame gapminder1
gapminder1['lifeexp_month1'] = gapminder1['lifeexp'] * 12

# generates the variable lifeexp * 12 and assigns it to the DataFrame gapminder1 using an anonymous function
gapminder1['lifeexp_month2'] = gapminder1['lifeexp'].apply(lambda x: x * 12)

# generates the variable lifeexp * 12 and assigns it to the DataFrame gapminder1 by first defining a function
def monthly(x):
    res = x * 12
    return(res)

# if a column is not selected it applies it to the whole DataFrame
gapminder1['lifeexp_month3'] = gapminder1['lifeexp'].apply(monthly)

#%%
'''8.a'''
df_europe = gapminder[(gapminder['continent'] == "Europe")].copy()
df_europe.reset_index(drop=True, inplace=True)

'''8.b'''
# groups by country and applies the growth in an anonymous function
df_europe['gdpgrowth'] = df_europe.groupby('country')['gdpPercap'].apply(lambda x: (x / x.shift(1) - 1))

'''8.c'''
df_europe.dropna(subset=['gdpgrowth'], inplace=True) # selects a subset (gdpgrowth) and drops them in-place
df_europe.dropna() # drops all NAs (row and column)

'''8.d'''
# grouped mean by country
df_europe.groupby('country').mean()
# describe by country, grouped
desc_stat = df_europe.groupby(['country']).describe()

'''8.e'''
# exports the descriptive statistics to excel
desc_stat.to_excel("desc_stat_europe.xlsx")

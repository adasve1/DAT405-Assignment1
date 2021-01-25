import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# load data frames
dfGDP = pd.read_csv("gdp-per-capita.csv")
dfLifeExp = pd.read_csv("life-expectancy.csv")


################################################
# d) Which countries have a higher life expectancy than one std dev above the mean?
################################################

lifeExp2016 = dfLifeExp.loc[dfLifeExp['Year'] == 2016]
# print(len(lifeExp2016))

# Remove entities without country code (continents)
lifeExp2016['Code'].replace('', np.nan, inplace=True)
lifeExp2016 = lifeExp2016.dropna(subset=['Code'])
lifeExp2016 = lifeExp2016.loc[lifeExp2016['Entity'] != "World"]

# Find mean and std dev
detailsLifeExp = lifeExp2016.describe()
mean = detailsLifeExp.iloc[1, 1]
std = detailsLifeExp.iloc[2, 1]

# Find countries with a higher (lower) life exp than mean + (-) std dev
meanPlusStd = mean + std
meanMinusStd = mean - std

# 42 (44) countries with high (low) life exp
highLifeExp = lifeExp2016.loc[lifeExp2016['Life expectancy'] > meanPlusStd]
lifeExpAboveMean = lifeExp2016.loc[lifeExp2016['Life expectancy'] > mean]
lowLifeExp = lifeExp2016.loc[lifeExp2016['Life expectancy'] < meanMinusStd]
# print(highLifeExp)
# print(len(highLifeExp))


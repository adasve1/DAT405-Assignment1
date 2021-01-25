import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from Q1d import highLifeExp, lifeExp2016, lifeExpAboveMean

# load data frames
dfGDP = pd.read_csv("gdp-per-capita.csv")
dfLifeExp = pd.read_csv("life-expectancy.csv")


################################################
# e) Which countries have a high life expectancy but low GDP?
################################################


gdp2016 = dfGDP.loc[dfGDP['Year']==2016]

# Remove entities without country code (continents)
gdp2016['Code'].replace('', np.nan, inplace=True)
gdp2016 = gdp2016.dropna(subset=['Code'])
gdp2016 = gdp2016.loc[gdp2016['Entity'] != "World"]

# Find low gdp
detailsGDP = gdp2016.describe()
fiftyPerc = detailsGDP.iloc[5,1]
seventyfivePerc = detailsGDP.iloc[6,1]


# Approach 1, use lifeExp > mean+std, gdp < 50 percentile, 0 countries
#Countries with low gdp
lowGDPApproach1 = gdp2016.loc[gdp2016['Real GDP per capita in 2011US$, multiple benchmarks (Maddison Project Database (2018))'] < fiftyPerc]
# print(lowGDP)

# Countries with high life exp and low GDP
merged = highLifeExp.merge(lowGDPApproach1, how='inner', on='Entity')
# print(merged)

# Approach 2, use lifeExp > mean+std, gdp < 75 percentile, 1 country - Greece
lowGDPApproach2 = gdp2016.loc[gdp2016['Real GDP per capita in 2011US$, multiple benchmarks (Maddison Project Database (2018))'] < seventyfivePerc]

# Countries with high life exp and low GDP
merged = highLifeExp.merge(lowGDPApproach2, how='inner', on='Entity')
# print(merged)


# Approach 3, use lifeExp>mean, gdp < 50 percentile
mergedApproach3 = lifeExpAboveMean.merge(lowGDPApproach1, how='inner', on='Entity')

with pd.option_context("display.max_rows", None, "display.max_columns", None):
    print(mergedApproach3)



import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from Q1d import lifeExp2016
from Q1e import gdp2016, detailsGDP


# load data frames
dfGDP = pd.read_csv("gdp-per-capita.csv")
dfLifeExp = pd.read_csv("life-expectancy.csv")

################################################
# g) Related to question f, what would happen if you use GDP per capita as an indicator of strong economy?
# Explain the results you obtained, and discuss any insights you get from comparing the results of g and f.
################################################

# Look at GDP > mean+std dev
mean = detailsGDP.iloc[1,1]
std = detailsGDP.iloc[2,1]
meanPlusStd = mean+std

highGdpPerCapita2016 = gdp2016.loc[gdp2016['Real GDP per capita in 2011US$, multiple benchmarks (Maddison Project Database (2018))'] > meanPlusStd]

# Merge with life exp

highGdpPerCapitaAndLifeExp2016 = lifeExp2016.merge(highGdpPerCapita2016,how='inner',on='Entity')

fig,ax = plt.subplots()
ax.scatter(highGdpPerCapitaAndLifeExp2016.iloc[:,6],highGdpPerCapitaAndLifeExp2016.iloc[:,3])
for i in range(len(highGdpPerCapitaAndLifeExp2016.iloc[:,0])):
    ax.annotate(highGdpPerCapitaAndLifeExp2016.iloc[i,0],(highGdpPerCapitaAndLifeExp2016.iloc[i,6], highGdpPerCapitaAndLifeExp2016.iloc[i,3]),fontsize=6)

plt.xlabel('GDP per capita [$]')
plt.ylabel('Life expectancy [Years]')
plt.title('Life expectancy for countries with high GDP per capita')
fig.savefig("highGdpPerCapita_relatedLifeExp.pdf")
# plt.show()


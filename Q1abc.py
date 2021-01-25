import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy.polynomial.polynomial as poly

# load data frames
dfGDP = pd.read_csv("gdp-per-capita.csv")
dfLifeExp = pd.read_csv("life-expectancy.csv")

##############################################
# Q1, a)
##############################################

# Select data averaged over the world
dfLifeExpWorld = dfLifeExp.loc[dfLifeExp['Entity'] == "World"]
dfGDPWorld = dfGDP.loc[dfGDP['Entity'] == "World"]


# Find the years that are common in the data sets
# Combine... holds common years, lifeExpInd and gdpInd holds indices for common values
# CombineLifeExpAndGdpForWorld, lifeExpInd, gdpInd =  np.intersect1d(dfLifeExpWorld.iloc[:, 2], dfGDPWorld.iloc[:, 2], return_indices=True)

# Select GDP and life expectancy for the indices that where common
# commonGdp = dfGDPWorld.iloc[gdpInd].iloc[:,3]
# commonLifeExp = dfLifeExpWorld.iloc[lifeExpInd].iloc[:,3]

# Find data from common years
def findCommonYears(dfLifeExp, dfGdp):
    commonYears, lifeExpInd, gdpInd = np.intersect1d(dfLifeExp.iloc[:, 2], dfGdp.iloc[:, 2], return_indices=True)
    commonLifeExp = dfLifeExp.iloc[lifeExpInd].iloc[:, 3]
    commonGdp = dfGdp.iloc[gdpInd].iloc[:, 3]
    return commonLifeExp, commonGdp;


# create the plot with Life expectancy vs GDP
# plt.scatter(commonGdp,commonLifeExp)
# plt.title('Life expectancy vs GDP (world avergage)')
# plt.xlabel('GDP [$]')
# plt.ylabel('Life expectancy [Years]')
# plt.show()

##############################################
# Compare countries China, United States, United Kingdom, Afghanistan, Chile, Gambia

# Select GDP and life expectancy for each country
# GDP
chinaGDP = dfGDP.loc[dfGDP['Entity'] == "China"]
usaGDP = dfGDP.loc[dfGDP['Entity'] == "United States"]
ukGDP = dfGDP.loc[dfGDP['Entity'] == "United Kingdom"]
afgGDP = dfGDP.loc[dfGDP['Entity'] == "Afghanistan"]
chileGDP = dfGDP.loc[dfGDP['Entity'] == "Chile"]
gambiaGDP = dfGDP.loc[dfGDP['Entity'] == "Gambia"]

# Life expectancy
chinaLifeExp = dfLifeExp.loc[dfLifeExp['Entity'] == "China"]
usaLifeExp = dfLifeExp.loc[dfLifeExp['Entity'] == "United States"]
ukLifeExp = dfLifeExp.loc[dfLifeExp['Entity'] == "United Kingdom"]
afgLifeExp = dfLifeExp.loc[dfLifeExp['Entity'] == "Afghanistan"]
chileLifeExp = dfLifeExp.loc[dfLifeExp['Entity'] == "Chile"]
gambiaLifeExp = dfLifeExp.loc[dfLifeExp['Entity'] == "Gambia"]

# The common values that should be plotted
lifeExpChina, gdpChina = findCommonYears(chinaLifeExp, chinaGDP)
lifeExpUsa, gdpUsa = findCommonYears(usaLifeExp, usaGDP)
lifeExpUk, gdpUk = findCommonYears(ukLifeExp, ukGDP)
lifeExpAfg, gdpAfg = findCommonYears(afgLifeExp, afgGDP)
lifeExpChile, gdpChile = findCommonYears(chileLifeExp, chileGDP)
lifeExpGambia, gdpGambia = findCommonYears(gambiaLifeExp, gambiaGDP)

plt.scatter(gdpChina, lifeExpChina, color='red', alpha=0.4, label='China', marker=".")
plt.scatter(gdpUsa, lifeExpUsa, color='blue', alpha=0.4, label='United States', marker="1")
plt.scatter(gdpUk, lifeExpUk, color='orange', alpha=0.5, label='United Kingdom', marker="d")
plt.scatter(gdpAfg, lifeExpAfg, color='purple', alpha=0.4, label='Afghanistan', marker="*")
plt.scatter(gdpChile, lifeExpChile, color='black', alpha=0.4, label='Chile', marker="X")
plt.scatter(gdpGambia, lifeExpGambia, color='green', alpha=0.4, label='Gambia', marker="+")
plt.legend(loc="lower right")
plt.xlabel('GDP [$]')
plt.ylabel('Life expectancy [Years]')
plt.title('Life expectency vs GDP for different countries')
# plt.show()

# For all countries
dfGdp2016 = dfGDP.loc[dfGDP['Year']==2016]
dfLifeExp2016 = dfLifeExp.loc[dfLifeExp['Year']==2016]

# Remove entities without country code (continents)
dfLifeExp2016['Code'].replace('', np.nan, inplace=True)
dfLifeExp2016 = dfLifeExp2016.dropna(subset=['Code'])
dfLifeExp2016 = dfLifeExp2016.loc[dfLifeExp2016['Entity'] != "World"]

dfGdp2016['Code'].replace('', np.nan, inplace=True)
dfGdp2016 = dfGdp2016.dropna(subset=['Code'])
dfGdp2016 = dfGdp2016.loc[dfGdp2016['Entity'] != "World"]

# merge
gdpAndlifeExp2016 = dfGdp2016.merge(dfLifeExp2016,on='Entity')

# Remove outlier, i.e. Qatar
gdpAndlifeExp2016 = gdpAndlifeExp2016.loc[gdpAndlifeExp2016['Entity'] != "Qatar"]

# create the plot with Life expectancy vs GDP

gdpAndLife, ax = plt.subplots()
ax.scatter(gdpAndlifeExp2016.iloc[:,3], gdpAndlifeExp2016.iloc[:,6])
plt.title('Life expectancy vs GDP ')
plt.xlabel('GDP [$]')
plt.ylabel('Life expectancy [Years]')
gdpAndLife.savefig('gdpVsLife.pdf')
# plt.show()

# With regression
# Polyfit
def polyFit(xVal, yVal, degree):
    x_new = np.linspace(xVal.min(), xVal.max())
    coefs = poly.polyfit(xVal, yVal, degree)
    ffit = poly.polyval(x_new, coefs)
    plt.plot(x_new, ffit, color='black')

polyFit(gdpAndlifeExp2016.iloc[:,3], gdpAndlifeExp2016.iloc[:,6], 2)
gdpAndLife.savefig('gdpVsLife_withReg.pdf')

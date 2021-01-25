import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from Q1d import lifeExp2016

dfGdp = pd.read_csv('gross-domestic-product.csv')



################################################
# f) Does every strong economy (normally indicated by GDP) have high life expectancy?
################################################

# Use year 2016
dfGdp2016 = dfGdp.loc[dfGdp['Year']==2016]

# Clean the data (no 'Code')
dfGdp2016['Code'].replace('', np.nan, inplace=True)
dfGdp2016 = dfGdp2016.dropna(subset=['Code'])
dfGdp2016 = dfGdp2016.loc[dfGdp2016['Entity'] != "World"]

# Look at GDP > 75% rather than from the std dist since US increases mean and std
detailsGdp2016 = dfGdp2016.describe()
mean = detailsGdp2016.iloc[1,1]
std = detailsGdp2016.iloc[2,1]
meanPlusStd = mean+std
# print(meanPlusStd)
seventyFivePerc = detailsGdp2016.iloc[6,1]
highGdp2016 = dfGdp2016.loc[dfGdp2016['GDP (constant 2010 US$)'] > meanPlusStd]

# Merge to look at both GDP and life exp
gdpAndLifeExp = lifeExp2016.merge(highGdp2016,how='inner', on='Entity')

with pd.option_context("display.max_rows", None, "display.max_columns", None):
    print(gdpAndLifeExp)


fig,ax = plt.subplots()
ax.scatter(gdpAndLifeExp.iloc[:,6],gdpAndLifeExp.iloc[:,3])
for i in range(len(gdpAndLifeExp.iloc[:,0])):
    ax.annotate(gdpAndLifeExp.iloc[i,0],(gdpAndLifeExp.iloc[i,6], gdpAndLifeExp.iloc[i,3]),fontsize=6)

plt.xlabel('GDP [$]')
plt.ylabel('Life expectancy [Years]')
plt.title('Life expectancy for countries with high GDP')
fig.savefig("highGdp_relatedLifeExp.pdf")
# plt.show()

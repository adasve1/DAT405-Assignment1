import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy.polynomial.polynomial as poly


#####################################
# Suicide vs education
#####################################
# load data frames
dfSuicide = pd.read_csv('suicide-death-rates.csv')
dfEducation = pd.read_csv('mean-years-of-schooling.csv')

# Choose data from year 2017
dfSuicide2017 = dfSuicide.loc[dfSuicide['Year'] == 2017]
dfEducation2017 = dfEducation.loc[dfEducation['Year'] == 2017]

# Find common countries, i.e merge together
suicideAndEducation2017 = dfSuicide2017.merge(dfEducation2017, on='Entity')

# Plot suicides vs education
suiVsEdu, ax = plt.subplots()
ax.scatter(suicideAndEducation2017.iloc[:, 6], suicideAndEducation2017.iloc[:, 3])
plt.xlabel('Mean years of schooling for people aged 25+')
plt.ylabel('Deaths from suicide per 100,000 people')
plt.title('Deaths from suicide vs mean years of education')
suiVsEdu.savefig('suicideVsEducation.pdf')

# Polyfit
def polyFit(xVal, yVal, degree):
    x_new = np.linspace(xVal.min(), xVal.max())
    coefs = poly.polyfit(xVal, yVal, degree)
    ffit = poly.polyval(x_new, coefs)
    plt.plot(x_new, ffit, color='black')


polyFit(suicideAndEducation2017.iloc[:, 6], suicideAndEducation2017.iloc[:, 3], 2)
suiVsEdu.savefig('suicideVsEducation_wRegression.pdf')
# plt.show()



#####################################
# Suicide vs GDP per capita
#####################################
# load data frames
dfGdpPerCapita = pd.read_csv('gdp-per-capita.csv')

# 2016 latest year
dfGdpPerCapita2016 = dfGdpPerCapita.loc[dfGdpPerCapita['Year'] == 2016]
dfSuicide2016 = dfSuicide.loc[dfSuicide['Year'] == 2016]

# Find common countries, i.e. merge together
suicideAndGdpPerCapita2016 = dfSuicide2016.merge(dfGdpPerCapita2016, on='Entity')

# Plot suicides vs GDP per capita
suiVsGdp, ax = plt.subplots()
ax.scatter(suicideAndGdpPerCapita2016.iloc[:, 6], suicideAndGdpPerCapita2016.iloc[:, 3])
plt.xlabel('GDP per capita [$]')
plt.ylabel('Deaths from suicide per 100,000 people')
plt.title('Deaths from suicide vs GDP per capita')
suiVsGdp.savefig('suicideVsGdp.pdf')
# plt.show()

# Polyfit
polyFit(suicideAndGdpPerCapita2016.iloc[:, 6], suicideAndGdpPerCapita2016.iloc[:, 3], 2)
suiVsGdp.savefig('suicideVsGdp_withRegression.pdf')




#####################################
# Life expectancy vs education
#####################################
# load data frames
dfLifeExp = pd.read_csv('life-expectancy.csv')

# Use 2017
dfLifeExp2017 = dfLifeExp.loc[dfLifeExp['Year']==2017]

# merge
lifeExpAndEdu2017 = dfLifeExp2017.merge(dfEducation2017, on='Entity')
# print((lifeExpAndEdu2017.info()))

# plot
lifeVsEdu, ax = plt.subplots()
ax.scatter(lifeExpAndEdu2017.iloc[:,6], lifeExpAndEdu2017.iloc[:,3])
plt.xlabel('Mean years of education')
plt.ylabel('Life expectancy')
plt.title('Life expectancy vs education')
lifeVsEdu.savefig('lifeVsEdu.pdf')

# Polyfit
polyFit(lifeExpAndEdu2017.iloc[:, 6], lifeExpAndEdu2017.iloc[:, 3], 2)
lifeVsEdu.savefig('lifeVsEdu_withRegression.pdf')


#####################################
# Total share of income to richest 10% vs Corruption
#####################################
# load data frames
dfIncome = pd.read_csv('income-share-held-by-richest-10.csv')
dfCorruption = pd.read_csv('TI-corruption-perception-index.csv')

# Use 2014
dfIncome2014 = dfIncome.loc[dfIncome['Year']==2014]
dfCorruption2014 = dfCorruption.loc[dfCorruption['Year']==2014]

# merge
incomeAndCorruption = dfIncome2014.merge(dfCorruption2014, on='Entity')
print(incomeAndCorruption.info())

# plot
incomeVsCorr, ax = plt.subplots()
ax.scatter(incomeAndCorruption.iloc[:,6], incomeAndCorruption.iloc[:,3])
plt.xlabel('Corruption index')
plt.ylabel('Income share held by richest 10%')
plt.title('Income vs corruption')
incomeVsCorr.savefig('incomeVsCorr.pdf')

# polyfit
polyFit(incomeAndCorruption.iloc[:,6], incomeAndCorruption.iloc[:,3], 2)
incomeVsCorr.savefig('incomeVsCorr_withRegression.pdf')

# Power to the people?











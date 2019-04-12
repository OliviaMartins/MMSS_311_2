import pandas as pd
import numpy as np
import statsmodels.api as sm
import os
import math
import matplotlib.pyplot as plt
import seaborn as sns
#Question 1
#(a)
vec = np.array([1, 2, 3, 4, 5])

#(b)
Mindy = 12

#(c)
m = np.array([[1, 2, 3], [4, 5, 6]])
print(m)

#(d)
n = np.array([[1, 3, 5], [2, 4, 6]])
print(n)

#(e)
a = np.ones([10,10], dtype = int)
print(a)

#(f)
vecs = np.array(["THIS", "IS", "A", "VECTOR"])
print(vecs)

#(g)
def sum_func(a, b, c):
    sum = a+b+c
    return sum
#tests
print(sum_func(1, 2, 3))
print(sum_func(1, 2, Mindy))


#(h)
def ten_func(number):
    if number<= 10:
        return "Yes"
    else:
        return "No"
#tests
print(ten_func(5))
print(ten_func(20))

#(i)
g = np.random.normal(10, 1, 1000)

#(j)
y = np.random.normal(5, 0.5, 1000)

#(k)
x = []
for j in range(0, 1000):
    i = 0
    ran_array = []
    for i in range (1, 10):
        ran_num = np.random.choice(g)
        ran_array.append(ran_num)
    avg = np.mean(ran_array)
    x.append(avg)


#(l)
dataq1 = pd.DataFrame(y, columns=['y'])
dataq1['x'] = x
dataq1['const'] = 1
model = sm.OLS(endog=dataq1['y'], exog=dataq1[['x', 'const']]).fit()
print(model.summary())

#Question 2
#(a)
os.chdir('/Users/OliviaMartins/Documents/MMSS_311-2/hw0')
dataq2=pd.read_csv("pums_chicago.csv")

#(b)
var = len(dataq2.columns)
print(var)
#there are 204 variables in the dataset

#(c)
mean_pincp = dataq2['PINCP'].mean()
print('The mean annual income, PINCP, is $' +str(mean_pincp))
#the mean annual income is $38247.62

#(d)
pincp_log = []
for val in dataq2['PINCP']:
    if val>0:
        log_val = math.log(val)
    if val<=0:
        log_val = 'NaN'
    pincp_log.append(log_val)
dataq2['PINCP_LOG'] = pincp_log
#NaN values were produced where PINCP is less than or equal to zero because
#natural log is only defined for values greater than zero

#(e)
grad_dummy = []
for val in dataq2['SCHL']:
    if val>=22:
        grad_dummy.append('grad')
    else:
        grad_dummy.append('no grad')
dataq2['GRAD.DUMMY'] = grad_dummy

#(f)
dataq2.drop('SERIALNO', axis=1)

#(g)
dataq2.to_csv('new_data.csv')

#(h)
emp = dataq2[dataq2['ESR'].isin([1, 2])]
unemp = dataq2[dataq2['ESR'] == 3]
af = dataq2[dataq2['ESR'].isin([4, 5])]
nilf = dataq2[dataq2['ESR'] == 6]
young = dataq2[dataq2['ESR'].astype(str) == 'b']

#(i)
empaf = dataq2[dataq2['ESR'].isin([1, 2, 4, 5])]

#(j)
employed_af = empaf[['AGEP', 'RAC1P', 'PINCP_LOG']]

#(k (i))
mean_jwmnp = dataq2['JWMNP'].mean()
print(mean_jwmnp)

median_jwmnp = dataq2['JWMNP'].median()
print(median_jwmnp)

percentile_jwmnp = dataq2['JWMNP'].quantile(0.8)
print(percentile_jwmnp)

#(k (ii))
corr = dataq2['JWMNP'].corr(dataq2['WAGP'])
print(corr)

#(k (iii))
dataq2[['AGEP', 'PINCP_LOG']].plot.scatter
plt.scatter(dataq2['AGEP'], dataq2['PINCP_LOG'])
plt.xlabel('Age')
plt.ylabel('Log Income')

#(k (iv))
plt.savefig('q2plot.pdf')

#(k (v))
crstb = pd.crosstab(dataq2['RAC1P'], dataq2['ESR'])
#(k (vi))
dataq2['const'] = 1
reg = sm.OLS(endog=dataq2['WAGP'], exog=dataq2[['WKHP', 'const']], missing = 'drop').fit()
print(reg.summary())

#(k (vii))
#please see R script for the graph associated with this regression

#(l (i))
dfmtcars = pd.read_csv("mtcars.csv")
x = dfmtcars['wt']
x = sm.add_constant(x)
y = dfmtcars['mpg']
regmtcars = sm.OLS(y, x).fit()
print(regmtcars.summary())

#(l (ii))
autodf = dfmtcars[dfmtcars['am']==1]
mandf = dfmtcars[dfmtcars['am']==0]
x1 = autodf['wt']
x1 = sm.add_constant(x)
y1 = autodf['mpg']
model1 = sm.OLS(y1, x1).fit()
x2 = mandf['wt']
x2 = sm.add_constant(x)
y2 = mandf['mpg']
model2 = sm.OLS(y2, x2).fit()
print(model1.summary())
print(model2.summary())

#(l (iii))
dfmtcars['log_hp'] = np.log(dfmtcars['hp'])
y3 = dfmtcars['mpg']
x3 = dfmtcars['log_hp']
x3 = sm.add_constant(x)
model3 = sm.OLS(y3, x3).fit()
print(model3.summary())

#(m)
#please see R script for part m (requires ggplot)

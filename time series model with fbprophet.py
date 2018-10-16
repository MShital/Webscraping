# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 13:02:39 2018

@author: admin
"""

import pandas as pd          
import numpy as np          # For mathematical calculations
import matplotlib.pyplot as plt  # For plotting graphs
from datetime import datetime    # To access datetime
from pandas import Series        # To work on series
#%matplotlib inline
import warnings                   # To ignore the warnings
warnings.filterwarnings("ignore")

train=pd.read_csv("Train_SU63ISt.csv")
test=pd.read_csv("Test_0qrQsBZ.csv")

train_original=train.copy()
test_original=test.copy()
train.columns, test.columns


#Let’s look at the data types of each feature.

train.dtypes, test.dtypes

#Now we will see the shape of the dataset.
train.shape, test.shape
#((18288, 3), (5112, 2))

train['Datetime'] = pd.to_datetime(train.Datetime,format='%d-%m-%Y %H:%M') 
test['Datetime'] = pd.to_datetime(test.Datetime,format='%d-%m-%Y %H:%M') 
test_original['Datetime'] = pd.to_datetime(test_original.Datetime,format='%d-%m-%Y %H:%M')
train_original['Datetime'] = pd.to_datetime(train_original.Datetime,format='%d-%m-%Y %H:%M')


##We made some hypothesis for the effect of hour, day, month and year on the passenger count. So, let’s extract the year, month, day and hour from the Datetime to validate our hypothesis.

for i in (train, test, test_original, train_original):
    i['year']=i.Datetime.dt.year 
    i['month']=i.Datetime.dt.month 
    i['day']=i.Datetime.dt.day
    i['Hour']=i.Datetime.dt.hour 
    
    ##We made a hypothesis for the traffic pattern on weekday and weekend as well. So, let’s make a weekend variable to visualize the impact of weekend on traffic.

#We will first extract the day of week from Datetime and then based on the values we will assign whether the day is a weekend or not.

#Values of 5 and 6 represents that the days are weekend.

train['day of week']=train['Datetime'].dt.dayofweek
temp = train['Datetime']

#Let’s assign 1 if the day of week is a weekend and 0 if the day of week in not a weekend.

def applyer(row):
    if row.dayofweek == 5 or row.dayofweek == 6:
        return 1
    else:
        return 0

temp2 = train['Datetime'].apply(applyer)
train['weekend']=temp2


#Let’s look at the time series.

train.index = train['Datetime'] # indexing the Datetime to get the time period on the x-axis.
df=train.drop('ID',1)           # drop ID variable to get only the Datetime on x-axis.
ts = df['Count']
plt.figure(figsize=(16,8))
plt.plot(ts, label='Passenger Count')
plt.title('Time Series')
plt.xlabel("Time(year-month)")
plt.ylabel("Passenger count")
plt.legend(loc='best')


#Our first hypothesis was traffic will increase as the years pass by. So let’s look at yearly passenger count.

train.groupby('year')['Count'].mean().plot.bar()

#We see an exponential growth in the traffic with respect to year which validates our hypothesis.

#Our second hypothesis was about increase in traffic from May to October. So, let’s see the relation between count and month.

train.groupby('month')['Count'].mean().plot.bar()

temp=train.groupby(['year', 'month'])['Count'].mean()
temp.plot(figsize=(15,5), title= 'Passenger Count(Monthwise)', fontsize=14)
#Let’s look at the daily mean of passenger count.

train.groupby('day')['Count'].mean().plot.bar()
#We also made a hypothesis that the traffic will be more during peak hours. So let’s see the mean of hourly passenger count.

train.groupby('Hour')['Count'].mean().plot.bar()

#Let’s try to validate our hypothesis in which we assumed that the traffic will be more on weekdays.

train.groupby('weekend')['Count'].mean().plot.bar()

#Note - 0 is the starting of the week, i.e., 0 is Monday and 6 is Sunday.

train.groupby('day of week')['Count'].mean().plot.bar()
train=train.drop('ID',1)

train.Timestamp = pd.to_datetime(train.Datetime,format='%d-%m-%Y %H:%M') 
train.index = train.Timestamp

###https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.resample.html
# Hourly time series
hourly = train.resample('H').mean()

# Converting to daily mean
daily = train.resample('D').mean()

# Converting to weekly mean
weekly = train.resample('W').mean()

# Converting to monthly mean
monthly = train.resample('M').mean()

#Let’s look at the hourly, daily, weekly and monthly time series.

fig, axs = plt.subplots(4,1)

hourly.Count.plot(figsize=(15,8), title= 'Hourly', fontsize=14, ax=axs[0])
daily.Count.plot(figsize=(15,8), title= 'Daily', fontsize=14, ax=axs[1])
weekly.Count.plot(figsize=(15,8), title= 'Weekly', fontsize=14, ax=axs[2])
monthly.Count.plot(figsize=(15,8), title= 'Monthly', fontsize=14, ax=axs[3])

plt.show()



test.Timestamp = pd.to_datetime(test.Datetime,format='%d-%m-%Y %H:%M') 
test.index = test.Timestamp 

# Converting to daily mean
test = test.resample('D').mean()

train.Timestamp = pd.to_datetime(train.Datetime,format='%d-%m-%Y %H:%M') 
train.index = train.Timestamp

# Converting to daily mean
train = train.resample('D').mean()




################usibg facebook prophet
##To install the package
#conda install -c conda-forge fbprophet
#https://anaconda.org/conda-forge/fbprophet
#https://www.analyticsvidhya.com/blog/2018/05/generate-accurate-forecasts-facebook-prophet-python-r/
# Importing datasets
import pandas as pd
import numpy as np
from fbprophet import Prophet
# Read train and test
train = pd.read_csv('Train_SU63ISt.csv')
test = pd.read_csv('Test_0qrQsBZ.csv')

# Convert to datetime format
train['Datetime'] = pd.to_datetime(train.Datetime,format='%d-%m-%Y %H:%M') 
test['Datetime'] = pd.to_datetime(test.Datetime,format='%d-%m-%Y %H:%M')
train['hour'] = train.Datetime.dt.hour
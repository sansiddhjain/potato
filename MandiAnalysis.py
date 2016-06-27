import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame, Series
import time
import datetime
from datetime import datetime


start_day = pd.to_datetime('2004-01-01',format = '%Y-%m-%d')
end_day = pd.to_datetime('2015-12-01',format = '%Y-%m-%d')


df_gm = pd.read_csv('gurgaon.csv')
df_gm = df_gm[df_gm['City'] =='Gurgaon']
df_gm['Date'] = pd.to_datetime(df_gm['Date'],dayfirst=True,infer_datetime_format=True)
# df_gm = df_gm.set_index('Date')
# print df_gm.index.dtype
df_gm['Month'] = df_gm['Date'].apply(lambda x: datetime(x.year,x.month,1))
df_gm_mon = df_gm.groupby('Month')
# print df_gm_mon.mean().index



df_rain = pd.read_csv('raindata.csv',index_col = 1)
df_rain_gloc = df_rain.groupby('SD_Name')
# print df_rain_gloc.get_group('HARYANA, DELHI & CHANDIGARH').T
df_rh_mon = DataFrame()



df_oil = pd.read_csv('oil-final.csv')
df_oil['Month'] = pd.to_datetime(df_oil['Month'],infer_datetime_format=True)
df_oil = df_oil.set_index('Month')
# print df_oil.index


df_wpi = pd.read_csv('potatoWPI.csv')
df_wpi['Month'] = pd.to_datetime(df_wpi['Month'],format = '%Y-%m-%d')
df_wpi = df_wpi.set_index('Month')
# print df_wpi.index

"""
# months = [1,2,3,4,5,6,7,8,9,10,11,12]
df_prod = pd.read_csv('haryanapotato.csv')
# df_prod['S'] = pd.to_datetime(df_wpi['Month'],format = '%Y-%m-%d')
df_prod['Year'] = df_prod['Year'].apply(lambda x: int(x[:5]))
# df_prod['Month'] = months
# df_prod = df_wpi.set_index('Month')
print df_prod
"""

df = pd.concat([df_gm_mon.mean()['Modal'].loc[start_day:end_day],df_oil['diesel_price'].loc[start_day:end_day],df_wpi['WPI'].loc[start_day:end_day]],axis = 1)

import statsmodels.formula.api as sm
result = sm.ols(formula="Modal ~ diesel_price + WPI", data=df).fit()
print (result.params)
print (result.summary())

# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from pandas.tseries.offsets import DateOffset
from statsmodels.tsa.arima_model import ARIMA
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
import os
try:
    os.chdir(os.path.join(os.getcwd(), './time_series'))
    print(os.getcwd())
except:
    pass

# %%
import os
# os.chdir('???')
# os.getcwd()


# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# %%
df = pd.read_csv('gov_use_month.csv')
df.head()
df.tail()


# %%
df['Month'] = pd.to_datetime(df['Month'])


# %%
df.set_index('Month', inplace=True)


# %%
df.head()


# %%
df.plot()


# %%
decomposition = seasonal_decompose(df['Use'], freq=12)
fig = plt.figure()
fig = decomposition.plot()
fig.set_size_inches(15, 8)
fig.savefig('decompose.png')


# %%
def check_adfuller(time_series):
    """
    Pass in a time series, returns ADF report
    """
    result = adfuller(time_series)
    print('Augmented Dickey-Fuller Test:')
    labels = ['ADF Test Statistic', 'p-value',
              '#Lags Used', 'Number of Observations Used']

    for value, label in zip(result, labels):
        print(label+' : '+str(value))

    if result[1] <= 0.05:
        print("Reject the null hypothesis. Data is stationary")
    else:
        print("Do not reject the null hypothesis. Data is not stationary ")


# %%
check_adfuller(df['Use'])


# %%
df['First Difference'] = df['Use'] - df['Use'].shift(1)
Fdiff = df['First Difference'].plot()



# %%
check_adfuller(df['First Difference'].dropna())


# %%
df['Second Difference'] = df['First Difference'] - \
    df['First Difference'].shift(1)



# %%
check_adfuller(df['Second Difference'].dropna())


# %%
df['Seasonal Difference'] = df['Use'] - \
    df['Use'].shift(12)
df['Seasonal Difference'].plot()
forSave = Fdiff.get_figure()
forSave.savefig('Seasondif.png')

# %%
check_adfuller(df['Seasonal Difference'].dropna())


# %%
df['Seasonal First Difference'] = df['First Difference'] - \
    df['First Difference'].shift(12)
df['Seasonal First Difference'].plot()
df['Seasonal First Difference'].plot().get_figure().savefig('Season1dif.png')

# %%
check_adfuller(df['Seasonal First Difference'].dropna())


# %%


# %%
fig_first_acf = plot_acf(df["First Difference"].dropna())
fig_first_acf.savefig('acf1.png')


# %%
fig_first_pacf = plot_pacf(df["First Difference"].dropna())
fig_first_pacf.savefig('pacf1.png')


# %%
fig_seasonal_first_acf = plot_acf(df["Seasonal First Difference"].dropna())
fig_seasonal_first_acf.savefig('acf2.png')


# %%
fig_seasonal_first_pacf = plot_pacf(df["Seasonal First Difference"].dropna())
fig_seasonal_first_pacf.savefig('pacf2.png')


# %%


# %%
fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(
    df['First Difference'].iloc[13:], lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(
    df['First Difference'].iloc[13:], lags=40, ax=ax2)


# %%
fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(
    df['Seasonal First Difference'].iloc[13:], lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(
    df['Seasonal First Difference'].iloc[13:], lags=40, ax=ax2)


# %%


# %%
model = sm.tsa.statespace.SARIMAX(
    df['Use'], order=(0, 1, 0), seasonal_order=(1, 1, 1, 12))
results = model.fit()
print(results.summary())


# %%
model = sm.tsa.statespace.SARIMAX(
    df['Use'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
results = model.fit()
print(results.summary())


# %%
results.resid.plot()


# %%
results.resid.plot(kind='kde')


# %%
df['forecast'] = results.predict(start=150, end=167, dynamic=True)
df[['Use', 'forecast']].plot(figsize=(12, 8))
df[['Use', 'forecast']].plot(figsize=(12, 8)).get_figure().savefig('predictself.png')


# %%


# %%
# predict after 1975
future_dates = [df.index[-1] + DateOffset(months=x) for x in range(0, 24)]
future_dates


# %%
future_dates_df = pd.DataFrame(index=future_dates[1:], columns=df.columns)
future_df = pd.concat([df, future_dates_df])
future_df.head()


# %%
future_df['forecast'] = results.predict(start=167, end=191, dynamic=True)
future_df[['Use', 'forecast']].plot(figsize=(12, 8))
future_df.tail(50)
future_df[['Use', 'forecast']].plot(figsize=(12, 8)).get_figure().savefig('predictfuture.png')

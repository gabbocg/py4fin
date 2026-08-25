# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 21:02:01 2021

@author: Habac
"""
#%% '''Yahoo Finance API'''
'''1.a'''
# imports pandas
import pandas as pd
# import numpy
import numpy as np
# import ytfinance
import yfinance as yf

# ticker
asset = "GME"

# downloads GameSpot's OHCL data
gme_ohcl_daily = yf.download(asset, start = "2015-01-01", end = "2021-03-01")

'''1.b'''
# brief descriptive statistics
gme_ohcl_daily.apply(lambda x: x.describe())

'''1.c'''
# extracts the year
gme_ohcl_daily['Year'] = gme_ohcl_daily.index.year
# extracts the month
gme_ohcl_daily['Month'] = gme_ohcl_daily.index.month
# extracts the day
gme_ohcl_daily['Day'] = gme_ohcl_daily.index.day

'''1.d'''
# selects the adj close
gme_close_daily = gme_ohcl_daily.loc[:,['Close']]

#%%'''Changes Over Time'''
'''2.a'''
# applies the diff() method
gme_close_daily['diff'] = gme_close_daily[['Close']].apply(lambda x: x.diff())

'''2.b'''
# applies the shift() method
gme_close_daily['close_t_1'] = gme_close_daily[['Close']].apply(lambda x: x.shift(1))

'''2.c'''
# divides (1) by (2)
gme_close_daily['returns'] = gme_close_daily['diff'] / gme_close_daily['close_t_1']

'''2.d'''
# uses the pct_change() method
gme_close_daily['pct_change'] = gme_close_daily[['Close']].apply(lambda x: x.pct_change(1))

#%% '''Basic Time Series Visualization'''
'''3.a'''
# imports matplotlib
import matplotlib.pyplot as plt

# line chart
fig1 = gme_ohcl_daily.loc[:,'Close'].plot(kind='line', figsize=(13,5), lw=2) # creates a line chart
fig1.grid(color='grey', linestyle=':')                                       # changes the grid style
fig1.set_title('GameSpot (GME) Closing Price', fontsize=14, y=1.00)          # adds title
fig1.set_xlabel('')                                                          # x-axis label
fig1.set_ylabel('Close')

# saves the chart under the name fig1.png
plt.savefig('fig1.png', dpi=300)

#%% '''Technical Analysis: Moving Average'''
'''3.a'''
# selects the closing price
tech_analysis = gme_ohcl_daily.loc[:,['Close']]

# 20-day rolling minimum
tech_analysis['Min'] = gme_ohcl_daily['Close'].rolling(window=20).min()
# 20-day moving average
tech_analysis['SMA1'] = gme_ohcl_daily['Close'].rolling(window=20).mean()
# 20-day rolling maximum
tech_analysis['Max'] = gme_ohcl_daily['Close'].rolling(window=20).max()

# drops NAs in-place
tech_analysis.dropna(inplace=True)

# filtered dataframe
df2 =  tech_analysis.loc[:,['Min','Close','SMA1','Max']][(tech_analysis.index >= "2020-01-01") & (tech_analysis.index <= "2020-09-08")]

fig2 = df2.plot(figsize=(13,5), style=['g--', 'b-', 'r--', 'g--'], lw=2)   # creates a line chart
fig2.grid(color='grey', linestyle=':')                                     # changes the grid style
fig2.set_title('GameSpot (GME) 20-Day Rolling', fontsize=14, y=1.00)       # adds title
fig2.set_xlabel('')                                                        # x-axis label
fig2.set_ylabel('Close')                                                   # y-axis label

# saves the chart under the name fig2.png
plt.savefig('fig2.png', dpi=300)

'''3.b'''
# 252-day moving average
tech_analysis['SMA2'] = gme_ohcl_daily['Close'].rolling(window=252).mean()
# position using np.where()
tech_analysis['Positions'] = np.where(tech_analysis['SMA1'] > tech_analysis['SMA2'], 1, -1)

# drops NAs in-place
tech_analysis.dropna(inplace=True)

# selects SM1, Close, SMA2 and Positions
df3 = tech_analysis.loc[:,['SMA1','Close','SMA2','Positions']][(tech_analysis.index >= "2020-01-01") & (tech_analysis.index <= "2020-09-08")]

# fig (figure) and ax1 (axis)
fig, ax1 = plt.subplots(figsize=(13,5)) # # creates a subplot

lns1 = ax1.plot(df3.loc[:,['SMA1']], color='green', label="SMA1", linestyle='--', lw=2) # creates a line chart
lns2 = ax1.plot(df3.loc[:,['Close']], color='blue', label="Close", linestyle='-', lw=2) # creates a line chart
lns3 = ax1.plot(df3.loc[:,['SMA2']], color='green', label="SMA2", linestyle='--', lw=2) # creates a line chart

# y-axis label
ax1.set_ylabel('Close')

# creates a second axis that shares the same axis as ax1
ax2 = ax1.twinx()

# creates a line chart for the secondary axis
lns4 = ax2.plot(df3.loc[:,['Positions']], color='red', label="Pos.", linestyle='--', lw=2)

# y-axis label (secondary)
ax2.set_ylabel('Positions')

# the line charts are added together
lns = lns1 + lns2 + lns3 + lns4
labs = [l.get_label() for l in lns] # extracts label

# legend settings
ax1.legend(lns, labs, loc=2, facecolor="white", shadow=True)

# grid settings
ax1.grid(color='grey', linestyle=':', axis='both')

# title
fig.suptitle('Technical Indicator: 20- and 252-Day Moving Average | GameSpot (GME)', fontsize=14, y=0.925)

# saves the chart under the name fig3.png
plt.savefig('fig3.png', dpi=300)

'''3.c'''
# imports plotly
import plotly.graph_objects as go

# filters the OHCL data
df_plotly = gme_ohcl_daily[(gme_ohcl_daily.index >= "2020-01-01") & (gme_ohcl_daily.index <= "2020-09-08")]

# plots candlestick
fig_plotly = go.Figure(data=[go.Candlestick(x=df_plotly.index,
                                            open=df_plotly['Open'],
                                            high=df_plotly['High'],
                                            low=df_plotly['Low'],
                                            close=df_plotly['Close'])])

# displays it
fig_plotly.show()

#%% '''Downloading Multiple Indices'''
'''4.a'''
# tickers to download
tickers = ['FB', 'AMZN', 'AAPL', 'NFLX', 'GOOG']

# downloads and stores them in a dictionary
FAANG = {i: yf.download(i, start = "2000-01-01", end = "2021-03-01", interval='1mo') for i in tickers}
# puts each closing price into a list
FAANG_Close = [k[['Close']].dropna().rename(columns={'Close':j}) for j, k in FAANG.items()]

# concatenates each DataFrame by index (column-wise)
df_concat = pd.concat(FAANG_Close, axis=1)

fig4 = df_concat.dropna().plot(figsize=(13,5), lw=2)                       # creates a line chart
fig4.grid(color='grey', linestyle=':')                                     # changes the grid style
fig4.set_title('Evolution of Closing Prices | FAANG', fontsize=14, y=1.00) # adds title
fig4.set_xlabel('')                                                        # x-axis label
fig4.set_ylabel('Close')                                                   # y-axis label

# saves the chart under the name fig4.png
plt.savefig('fig4.png', dpi=300)

'''4.b'''
# from columns to rows
df_melted = df_concat.melt(var_name="Symbol", value_name="Close", ignore_index=False)

# the df is checked
df_melted

'''4.c'''
# from rows to columns
df_pivoted = df_melted.pivot(columns='Symbol', values='Close')

# the df is checked
df_pivoted
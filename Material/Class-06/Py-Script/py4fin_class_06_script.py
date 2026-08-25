# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 21:02:01 2021

@author: Habac
"""
#%%''' Applications '''

'''1.a'''
import numpy as np
import pandas as pd 

# load indices
stocks = pd.read_pickle('stocks.pkl')

# load s&p 500
sp500 = pd.read_pickle('sp500.pkl')

# risk-free rate
Rf = pd.read_pickle('rfree.pkl')

#%%
'''2.a'''
def returns(x):
    
    '''
    Parameters
    ----------
    x : Array of dimension tx1
  
    Returns
    -------
    Arithmetic return of dimension (t-1)x1
    '''
    
    arithmetic_return = np.diff(x, axis = 0) / x[:-1]
    return(arithmetic_return)

#%%
'''3.a'''
# empty dictionary
dict_return = {}

for ticker, close in stocks.items():
    print('Computing return for ticker: ', ticker)
    dict_return[ticker] = returns(close)

#%%
'''4.a'''
# market return
Rm = returns(sp500)

# risk premium
Rm_Rf = Rm - Rf

#%%
'''5.a'''
# weights (sum to 1)
w = np.array([0.25, 0.25, 0.20, 0.20, 0.10]).reshape((-1,1))

def portfolio(x, w, rf):
    
    '''
    Parameters
    ----------
    x : Dictionary containing i arrays of dimension t1
    w : Weights of dimension i1
    rf: Risk-free rate of dimension t1
    
    Returns
    -------
    Weighted portfolio of dimension t1
    '''

    ret_list = []
    
    for name, r_i in x.items():
        ret_list.append(r_i)
        
    ret_mat = np.concatenate(ret_list, axis=1)
    rp = ret_mat.dot(w) - rf
    
    return(rp)
    
# excess return
Rp_Rf = portfolio(dict_return, w, Rf)    

#%%
'''6.a'''
# create the function
def ols(x,y):
    
    '''
    Parameters
    ----------
    x : ti matrix (Rm - Rf)
    y : ti matrix (Rp - Rf)
    
    Returns
    -------
    Alpha and Beta 
    '''

    m,n = x.shape
    
    x_with_ones = np.hstack((np.ones((m,1)),x))
    
    x_t_x = x_with_ones.T.dot(x_with_ones)
    inv_x_t_x = np.linalg.inv(x_t_x)
    
    betas = inv_x_t_x.dot(x_with_ones.T.dot(y))
    
    return(betas)

# parameters
ols(Rm_Rf,Rp_Rf)

#%%   
'''7.a'''
# beta portfolio
cov_var_mat = np.cov(np.concatenate([Rp_Rf,Rm_Rf], axis = 1), rowvar=False) 

cov_var_mat[0,1] / cov_var_mat[1,1]

#%%
'''7.b'''

def covariance(x,y):
    
    x_mean = x.mean()
    y_mean = y.mean()
    
    x_i = x - x_mean
    y_i = y - y_mean
    
    cov = sum(x_i * y_i) / (len(x) - 1)
        
    return(cov)

def variance(x):
    
    var = sum((x - x.mean()) ** 2) / (len(x) - 1)
    
    return(var)
    
covariance(Rm_Rf,Rp_Rf) / variance(Rm_Rf)

#%%
'''8.a'''

import statsmodels.api as sm

Rm_Rf_with_const = sm.add_constant(Rm_Rf)

mod = sm.OLS(Rp_Rf,Rm_Rf_with_const)
res = mod.fit()

print(res.summary(res))

res.params

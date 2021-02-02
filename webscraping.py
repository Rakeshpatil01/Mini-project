# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 20:01:09 2020

@author: RAKESH PATIL
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

tickers=["AXISBANK.NS"]

temp_dir=[]

for ticker in tickers:
    
    url="https://in.finance.yahoo.com/quote/"+ticker+'/financials?p='+ticker
    page = requests.get(url).text
    soup = BeautifulSoup(page,'lxml')
    tabl = soup.find_all(name="section",attrs={"data-test":"qsp-financial"})
    
    #it forr income statement
    for t in tabl:
        for i in range(0,250):
            rows=t.find(name="span",attrs={"data-reactid":i})
            if rows==None:
                continue
            else:
                temp_dir.append(rows.text)
                
    #getting balance statement 
    url="https://in.finance.yahoo.com/quote/"+ticker+'/balance-sheet?p='+ticker
    page = requests.get(url).text
    soup= BeautifulSoup(page,'lxml')

    tabl=soup.find_all(name="section",attrs={"data-test":"qsp-financial"})
    
    for t in tabl:
        for i in range(0,250):
            rows=t.find(name="span",attrs={"data-reactid":i})
            if rows==None:
                continue
            else:
                temp_dir.append(rows.text)   
    a = np.asarray(temp_dir[9:])
    a.resize(10,6)   
    
    #getting cash flow
    url="https://in.finance.yahoo.com/quote/"+ticker+'/cash-flow?p='+ticker
    page = requests.get(url).text
    soup=BeautifulSoup(page,'lxml')
    tabl=soup.find_all(name="section",attrs={"data-test":"qsp-financial"})
    
    for t in tabl:
        for i in range(0,250):
            rows=t.find(name="span",attrs={"data-reactid":i})
            if rows==None:
                continue
            else:
                temp_dir.append(rows.text)   
           
    #getting key statistics data
    url="https://in.finance.yahoo.com/quote/"+ticker+'/key-statistics?p='+ticker
    page = requests.get(url).text
    soup = BeautifulSoup(page,'lxml')
    tabl=soup.find_all(name="section",attrs={"data-test":"qsp-financial"})
    
    for t in tabl:
       for i in range(0,250):
            rows=t.find(name="span",attrs={"data-reactid":i})
            if rows==None:
                continue
            else:
                temp_dir.append(rows.text)   
                 
    #combining all extracted information
combined_financials = pd.DataFrame(temp_dir)
combined_financials.dropna(axis=1,inplace=True)
tickers = combined_financials.columns
print(combined_financials)
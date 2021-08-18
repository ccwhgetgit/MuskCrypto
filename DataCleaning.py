import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
import string 
from datetime import datetime
from nltk.sentiment import SentimentIntensityAnalyzer
from random import shuffle

import re 

data = pd.read_csv('TweetsElonMusk.csv')
price = pd.read_csv('DOGE-USD.csv')
priceBTC = pd.read_csv('BTC-USD.csv')



#step 1 : Data Cleaning 
data['tweet'] = data['tweet'].str.lower()


#need to extract the date - assumed to be within 1st Dec 2020 and 11th April 2021

withindate_price = (price['Date'] <= '2021-04-11') & (price['Date'] >= '2020-11-01')
price = price.loc[withindate_price]
price = price[['Date', 'Close', 'Volume']] #filtered


priceBTC = priceBTC.loc[(priceBTC['Date'] <= '2021-04-11') & (priceBTC['Date'] >= '2020-11-01')]
priceBTC = priceBTC[['Date', 'Close', 'Volume']]


english_punctuations = string.punctuation
punctuations_list = english_punctuations

def cleaning_punctuations(text):
    translator = str.maketrans('', '', punctuations_list)
    return text.translate(translator)

def cleaning_URLs(data):
    return re.sub('((www.[^s]+)|(https?://[^s]+))',' ',data)

def remove_tags(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)
        
    return input_txt 

data['tweet'] = np.vectorize(remove_tags)(data['tweet'], "@[\w]*")
data['tweet'] = data['tweet'].apply(lambda x: cleaning_URLs(x))
data['tweet']= data['tweet'].apply(lambda x: cleaning_punctuations(x))


#Step 2 : Implementing a time period to filter out the tweets 

withindate_data = data['date'] >= '2020-11-01'
data = data.loc[withindate_data]
withindate_data2 = data['date'] <= '2021-04-11'
data = data.loc[withindate_data2]
data.sort_values(by = ['date'])
data.drop_duplicates()
data['date'] = pd.to_datetime(data['date'])
data.sort_values(by = 'date')
data = data[['date', 'tweet']]
data = data[::-1]
data.rename(columns = {'date':'Date'})

data
#Step 7 : Analysing Patterns 

bitcoin_sentiments = bitcoin_data


index = bitcoin_data.index
bitcoin_data_index = index.tolist()

column_names = ["Date", "avg_sentiment_btc"]
bitcoin_avg = pd.DataFrame(columns = column_names) 
sumcpd = 0 
length = 1 
counter = 0 

#able to extrat out the data but the logic s wrong 

for i in range(len(bitcoin_data) - 1):
    if ((bitcoin_sentiments.loc[bitcoin_data_index[i], 'date']) == (bitcoin_sentiments.loc[bitcoin_data_index[i + 1], 'date'])):
        length += 1
        sumcpd += bitcoin_sentiments.loc[bitcoin_data_index[i], 'compound']
    else: 
        
        bitcoin_avg.loc[counter, "Date"] = bitcoin_sentiments.loc[bitcoin_data_index[i], 'date']
        bitcoin_avg.loc[counter, "avg_sentiment_btc"] = float(sumcpd / length)
        
        sumcpd = 0 
        length = 1 
        counter += 1

#Step 7 : Analysing Patterns 

doge_sentiments = dogecoin_data

index = dogecoin_data.index
doge_data_index = index.tolist()

sumcpd = 0 
length = 1
counter = 0 

column_names = [['date','avg']]
avg_doge = pd.DataFrame(columns = column_names)



for i in range(len(dogecoin_data) - 1 ):
    if ((doge_sentiments.loc[doge_data_index[i], 'date']) == (doge_sentiments.loc[doge_data_index[i + 1], 'date'])):
        sumcpd += doge_sentiments.loc[doge_data_index[i], 'compound']
        length += 1
 
        
    else: 
        
        counter += 1
        
        #extract the dates to aggregate 
        avg_doge.loc[counter, 'date'] = doge_sentiments.loc[doge_data_index[i], 'date']
        avg_doge.loc[counter, 'avg'] = float(sumcpd/length)
       
        #extract the sentiment score 
        sumcpd += doge_sentiments.loc[doge_data_index[i], 'compound']
        avg_doge.loc[counter, 'avg'] = float(sumcpd/length)
        
        
        sumcpd = 0 
        length = 1

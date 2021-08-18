#Step 7 : Analysing Patterns 

bitcoin_sentiments = bitcoin_data


index = bitcoin_data.index
bitcoin_data_index = index.tolist()

column_names = ["Date", "avg_sentiment_btc", "number"]
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
        bitcoin_avg.loc[counter, "number"] = length
        
        sumcpd = 0 
        length = 1 
        counter += 1

#normalising the timestamp to remove the time within 
for i in range(bitcoin_avg.shape[0]):
    time = bitcoin_avg.loc[:, 'Date'][i]
    output = pd.to_datetime(time).date()
    bitcoin_avg.loc[:, 'Date'][i] = output


    
#Step 7 : Analysing Patterns 

doge_sentiments = dogecoin_data

index = dogecoin_data.index
doge_data_index = index.tolist()

sumcpd = 0 
length = 1
counter = 0 

column_names = [['date','avg', 'number']]
avg_doge = pd.DataFrame(columns = column_names)



for i in range(len(dogecoin_data) - 1 ):
    if ((doge_sentiments.loc[doge_data_index[i], 'date']) == (doge_sentiments.loc[doge_data_index[i + 1], 'date'])):
        sumcpd += doge_sentiments.loc[doge_data_index[i], 'compound']
        length += 1
 
        
    else: 
        
        counter += 1
        
        #extract the dates to aggregate 
        avg_doge.loc[counter, 'date'] = pd.to_datetime(doge_sentiments.loc[doge_data_index[i], 'date']).date()
        avg_doge.loc[counter, 'avg'] = float(sumcpd/length)
       
        #extract the sentiment score 
        sumcpd += doge_sentiments.loc[doge_data_index[i], 'compound']
        avg_doge.loc[counter, 'avg'] = float(sumcpd/length)
        avg_doge.loc[counter, 'number'] = length
        
        sumcpd = 0 
        length = 1
        
#For bitcoin


btc_graph = priceBTC[['Date', 'Close', 'Volume']].copy()
btc_graph['avg_sentiments'] = 0
btc_graph['Number'] = 0
btc_graph = btc_graph[::-1]

#transferring the avg_sentiments over based on their dates 
btc_graph = btc_graph.reset_index(drop = True)


for i in range(bitcoin_avg.shape[0]):
    a= bitcoin_avg['Date'][i].strftime("%Y-%m-%d")
    for j in range(btc_graph.shape[0]):
        b=  btc_graph.loc[j, 'Date']
        #print(bitcoin_avg['avg_sentiment_btc'][j])
       
        if (a == b):
           
            btc_graph.loc[j, "avg_sentiments"] = bitcoin_avg['avg_sentiment_btc'][i]
            btc_graph.loc[j, "Number"] = bitcoin_avg['number'][i]


            break;
       
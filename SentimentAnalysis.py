bitcoin_list = ['bitcoin', 'gold', 'boom', 'crypto', 'price', 'meme', 'coin']
dogecoin_list = ['dogecoin', 'shiba', 'inu', 'doge','gold', 'boom', 'crypto', 'price', 'meme', 'coin' ]
sia = SentimentIntensityAnalyzer()

#Segregating into bitcoin and dogecoin tweets 


#Bitcoin Tweets
bitcoin_store = []
bitcoin_date_list = []


for i in range(data.shape[0]): 
    sentence = data['tweet'][i]
    found = False
    list_res = sentence.split()
    for j in range(len(list_res)): 
        if list_res[j] in bitcoin_list: 
            found = True 
            bitcoin_store.append(i)
            bitcoin_date_list.append(i)
            break 



bitcoin_data = data.loc[bitcoin_store, :]
index = bitcoin_data.index
bitcoin_data_index = index.tolist()

bitcoin_data['negative'] = 0
bitcoin_data['positive'] = 0
bitcoin_data['neutral'] = 0
bitcoin_data['compound'] = 0
bitcoin_data['sentiment'] = 0

for i in range(len(bitcoin_data['tweet'])):
    sentence = data['tweet'][bitcoin_data_index[i]]
    bitcoin_data.loc[bitcoin_data_index[i], 'negative']= sia.polarity_scores(sentence).get('neg')
    bitcoin_data.loc[bitcoin_data_index[i], 'positive']= sia.polarity_scores(sentence).get('pos')
    bitcoin_data.loc[bitcoin_data_index[i], 'neutral']= sia.polarity_scores(sentence).get('neu')
    bitcoin_data.loc[bitcoin_data_index[i], 'compound']= sia.polarity_scores(sentence).get('compound')

    if sia.polarity_scores(sentence).get('compound') > 0: 
        bitcoin_data.loc[bitcoin_data_index[i], 'sentiment'] = 1
    elif sia.polarity_scores(sentence).get('compound') == 0: 
        bitcoin_data.loc[bitcoin_data_index[i], 'sentiment'] = 0
    else: 
        bitcoin_data.loc[bitcoin_data_index[i], 'sentiment'] = -1


#Dogecoin Tweets


dogecoin_store = []
dogecoin_date_list = []


for i in range(data.shape[0]): 
    sentence = data['tweet'][i]
    found = False
    list_res = sentence.split()
    for j in range(len(list_res)): 
        if list_res[j] in dogecoin_list: 
            found = True 
            dogecoin_store.append(i)
            dogecoin_date_list.append(i)
            break 

dogecoin_data = data.loc[dogecoin_store, :]
index = dogecoin_data.index
dogecoin_data_index = index.tolist()

dogecoin_data['negative'] = 0
dogecoin_data['positive'] = 0
dogecoin_data['neutral'] = 0
dogecoin_data['compound'] = 0
dogecoin_data['sentiment'] = 0

for i in range(len(dogecoin_data['tweet'])):
    sentence = data['tweet'][dogecoin_data_index[i]]
    dogecoin_data.loc[dogecoin_data_index[i], 'negative']= sia.polarity_scores(sentence).get('neg')
    dogecoin_data.loc[dogecoin_data_index[i], 'positive']= sia.polarity_scores(sentence).get('pos')
    dogecoin_data.loc[dogecoin_data_index[i], 'neutral']= sia.polarity_scores(sentence).get('neu')
    dogecoin_data.loc[dogecoin_data_index[i], 'compound']= sia.polarity_scores(sentence).get('compound')

    if sia.polarity_scores(sentence).get('compound') > 0: 
        dogecoin_data.loc[dogecoin_data_index[i], 'sentiment'] = 1
    elif sia.polarity_scores(sentence).get('compound') == 0: 
        dogecoin_data.loc[dogecoin_data_index[i], 'sentiment'] = 0
    else: 
        dogecoin_data.loc[dogecoin_data_index[i], 'sentiment'] = -1


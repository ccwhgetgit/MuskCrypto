#For dogecoin


doge_graph = price[['Date', 'Close', 'Volume']].copy()
doge_graph['avg_sentiments'] = 0
doge_graph['Number'] = 0
doge_graph = doge_graph[::-1]

#transferring the avg_sentiments over based on their dates 
doge_graph = doge_graph.reset_index(drop = True)


for i in range(1, avg_doge.shape[0]+1):
    a= str(avg_doge.loc[i,'date']).split()[1]
    for j in range(doge_graph.shape[0]):
        b =  doge_graph.loc[j, 'Date']
        if (a == b):
            doge_graph.loc[j, "avg_sentiments"] = str( avg_doge.loc[i,'avg']).split()[1]
            doge_graph.loc[j, "Number"] =  str( avg_doge.loc[i,'number']).split()[1]
            break;
doge_graph


plt.plot(doge_graph['Date'], normalize_data(doge_graph['Volume']), color = 'r', label = "Volume")
plt.plot(doge_graph['Date'], doge_graph['Number'].astype(int), color = 'b', linewidth = 0.5, label = "number of tweets")
plt.xticks(fontsize = 1)
plt.title('Number of Tweets v Volume of Dogecoin')
plt.xlabel('Date: Dec 2020 to April 2021')

plt.legend()
plt.show()




plt.plot(doge_graph['Date'], normalize_data(doge_graph['Close'].pct_change()*100), color = 'r', label = "Return Rate")
plt.plot(doge_graph['Date'], doge_graph['avg_sentiments'].astype(float), color = 'b', linewidth = 0.5, label = "average sentiments")
plt.xticks(fontsize = 1)
plt.title('Sentiment Analysis v Return Rate of Dogecoin')
plt.xlabel('Date: Dec 2020 to April 2021')

plt.legend()
plt.show()
def normalize_data(df):
    min = df.min()
    max = df.max()
    x = df 
    y = (x - min) / (max - min)
    
    return y

plt.plot(btc_graph['Date'], btc_graph['avg_sentiments'], color = 'b', linewidth = 2, label = "sentiment")
plt.plot(btc_graph['Date'], normalize_data(btc_graph['Close'].pct_change()*100), color = 'm', label = "Return")
plt.title('Sentiment Analysis v Return Rate of Bitcoin')
plt.xticks(fontsize = 1)
plt.xlabel('Date: Dec 2020 to April 2021')
plt.legend()
plt.show()

plt.plot(btc_graph['Date'], btc_graph['avg_sentiments'], color = 'b', linewidth = 2, label = "sentiment")
plt.plot(btc_graph['Date'], normalize_data(btc_graph['Close']), color = 'm', label = "Price")
plt.xticks(fontsize = 1)
plt.title('Sentiment Analysis v Price of Bitcoin')
plt.xlabel('Date: Dec 2020 to April 2021')

plt.legend()
plt.show()


plt.plot(btc_graph['Date'], btc_graph['avg_sentiments'], color = 'b', linewidth = 2, label = "sentiment")
plt.plot(btc_graph['Date'], normalize_data(btc_graph['Volume']), color = 'r', label = "Volume")

plt.xticks(fontsize = 1)
plt.title('Sentiment Analysis v Return Rate of Bitcoin')
plt.xlabel('Date: Dec 2020 to April 2021')

plt.legend()
plt.show()


plt.plot(btc_graph['Date'], normalize_data(btc_graph['Volume']), color = 'r', label = "Volume")
plt.plot(btc_graph['Date'], btc_graph['Number'], linewidth = 0.5, color = 'b', label = "Number of Tweets")


plt.xticks(fontsize = 1)
plt.title('Number of Tweets v Vol of Bitcoin')
plt.xlabel('Date: Dec 2020 to April 2021')


plt.legend()
plt.show()




plt.plot(btc_graph['Date'], btc_graph['Number'], color = 'b', linewidth = 0.5, label = "number of tweets")
plt.plot(btc_graph['Date'], normalize_data(btc_graph['Close']), color = 'm', label = "Price")

plt.xticks(fontsize = 1)
plt.title('Number of Tweets v Price of Bitcoin')
plt.xlabel('Date: Dec 2020 to April 2021')


plt.legend()
plt.show()


plt.plot(btc_graph['Date'], btc_graph['Number'], color = 'b', linewidth = 0.5, label = "number of tweets")
plt.plot(btc_graph['Date'], normalize_data(btc_graph['Volume']), color = 'r', label = "Volume")


plt.xticks(fontsize = 1)
plt.title('Number of Tweets v Volume of Bitcoin')
plt.xlabel('Date: Dec 2020 to April 2021')



plt.legend()
plt.show()


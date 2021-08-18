#Step 4 : Visualising the hike in price
plt.plot(price['Date'], price['Close'], color = 'b', linewidth = 2)
plt.xlabel('Days', fontsize = 14)
plt.xticks(fontsize = 1)
plt.ylabel('Price (USD)', fontsize = 14)
plt.title('Price of Dogecoin from Nov 2020 to April 2021')
plt.show()

plt.plot(priceBTC['Date'], priceBTC['Close'], color = 'b', linewidth = 2)
plt.xlabel('Days', fontsize = 14)
plt.xticks(fontsize = 1)
plt.ylabel('Price (USD)', fontsize = 14)
plt.title('Price of BTC from Nov 2020 to April 2021')
plt.show()

#Step 5 : Calculating the return rates for price of DogeCoin

return_doge = price['Close'].pct_change()*100
plt.plot(price['Date'], return_doge, color='b', linewidth=2)
plt.xlabel('Dates', fontsize=14)
plt.xticks(fontsize = 1)
plt.ylabel('Return Rates (%)', fontsize=14)
plt.title('Return Rate of Dogecoin from Nov 2020 to April 2021')
plt.show()

#Date for the price hike of Dogecoin

doge_df = pd.DataFrame(return_doge)
doge_df.columns = ['Return Rate']
index = doge_df.index
condition = doge_df['Return Rate'] == return_doge.max()
doge_index = index[condition].tolist()
date_of_highest_return = doge_index[0]
date_doge = price['Date'][date_of_highest_return]
date_doge

#Step 5 : Calculating the return rates for price of Bitcoin 

return_BTC = priceBTC['Close'].pct_change()*100
plt.plot(priceBTC['Date'], return_BTC,color='b', linewidth=2) 
plt.xlabel('Dates', fontsize=14)
plt.xticks(fontsize = 1)
plt.ylabel('Return Rates (%)', fontsize=14)
plt.title('Return Rate of BTC from Nov 2020 to April 2021')
plt.show()

#Date for the price hike 

BTC_df = pd.DataFrame(return_BTC)
BTC_df.columns = ['Return Rate']
index = BTC_df.index
condition = BTC_df['Return Rate'] == return_BTC.max()
BTC_index = index[condition].tolist()
date_of_highest_return = BTC_index[0]
date_BTC = price['Date'][date_of_highest_return]
date_BTC

#Step 6 : Visualising the volume 
plt.plot(price['Date'], price['Volume'], color = 'b', linewidth = 2)
plt.xlabel('Days', fontsize = 14)
plt.xticks(fontsize = 1)
plt.ylabel('Vol (million)', fontsize = 14)
plt.title('Volume of Dogecoin from Dec 2020 to April 2021')
plt.show()

#Date for the Volume Hike of Dogecoin

priceDogevol = price['Volume']
Doge_vol = pd.DataFrame(priceDogevol)
Doge_vol.columns = ['Vol Doge']
index = Doge_vol.index
condition = Doge_vol['Vol Doge'] == priceDogevol.max()
Doge_index = index[condition].tolist()
date_of_highest_return = Doge_index[0]
date_Doge = price['Date'][date_of_highest_return]
date_Doge


#Step 6 : Visualising the volume 

plt.plot(priceBTC['Date'], priceBTC['Volume'], color = 'b', linewidth = 2)
plt.xlabel('Days', fontsize = 14)
plt.xticks(fontsize = 1)
plt.ylabel('Vol (million)', fontsize = 14)
plt.title('Volume of Bitcoin from Dec 2020 to April 2021')
plt.show()

#Date for the Volume Hike of BTC

priceBTCvol = priceBTC[ 'Volume']
BTC_vol = pd.DataFrame(priceBTCvol)
BTC_vol.columns = ['Vol BTC']
index = BTC_vol.index
condition = BTC_vol['Vol BTC'] == priceBTCvol.max()
BTC_index = index[condition].tolist()
date_of_highest_return = BTC_index[0]
date_BTC = priceBTC['Date'][date_of_highest_return]
date_BTC







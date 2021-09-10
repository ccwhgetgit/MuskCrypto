# MuskCrypto
Sentiment Analysis on Musks's tweets between December 2020 and April 2021 and its impacts on DogeCoin and Bitcoin 



## The Musk Effect : Is it really the all powerful?

On 28 April 2021, the billionaire Elon Musk tweeted “The Dogefather”, spiraling the value of Dogecoin up by 32% from $0.27 to $0.34. Inspired by an internet meme featuring a shiba inu dog, a flurry of tweets by Musk on Twitter has injected value to the virtually worthless digital token to billions of dollars in market capitalization. Undeniably, we have witnessed the influence of Musk’s tweets  to mobilize financial markets, such as Tesla and Signal. This is because social media has introduced a new opportunity structure which has empowered individuals with the platform to express their opinions to the wider public sphere. 

As such, this was inspired by the desire to expound the relationship between social media activity and its influence on cryptocurrency markets. In particular, I would like to unravel on the following question: Is the Musk Effect really all that powerful? 

I analyzed Musk’s Twitter history between December 2020 and April 2021 and identified possible patterns with the market movement. The twitter dataset was selected from Kaggle which contained detailed information within the period of December 2020 and April 2021. Likewise, I explored cryptocurrency data matching this timeframe and broke down to the second intervals to elucidate the price trends thereafter.  

For the purpose of this analysis, I adopted the following approach: 
•	From the Cryptocurrency market: 
o	Bitcoin and Dogecoin were selected as the 2 currencies of interest due to the supposed hype from Musk’s Tweets and Tesla’s actions
	Daily Closing price (in USD) 
	Trading volume 

•	From Musk’s tweets: 
o	Only cryptocurrency-related tweets containing the key words were filtered out. 
o	The lists included the following: 
	bitcoin_list = ['bitcoin', 'gold', 'boom', 'crypto', 'price', 'meme', 'coin']
	dogecoin_list = ['dogecoin', 'shiba', 'inu', 'doge','gold', 'boom', 'crypto', 'price', 'meme', 'coin' ]
o	Subsequently, the data was cleaned to remove hashtags, URLs and any mentions, tweet links et cetera which may introduce errors. 


## Assumption
 
Based on the Efficient Market Hypothesis, I assume that market prices reflect all available information. This means that all market players have access to Musk’s tweets as a source of information and that prices adjust accordingly to accommodate such information. 



## Analysis on Dogecoin

Preliminary data analysis has revealed that Musk’s tweets were effective in spiraling the price of the meme-coin. This was supported by the spikes in price (+275.6%) and volume (+1095.4%) of the coin within a day from 28th January 2021 to 29th January 2021. It coincided with Musk’s post of a picture about Dogecoin, replacing the cover of the magazine ‘Vogue’ with ‘Dogue’. 

 
 
 
Figure 1 : Overall number of tweets, Price and Vol of Dogecoin, Dec 2020 to April 2021

However, a sharp drop in the volume of dogecoin was noted immediately between 29 and 30 January 2021 due to competition from the stock market where meme-stocks such as GameStop, AMC and Blackberry experienced a Reddit-driven surge , causing a short squeeze in its price. As a result, there was a 65.6% drop in the volume and 40.3% fall in the price of dogecoin traded between these 2 days. 

What’s more interesting is to note the market’s gradual adaptation to Musk’s constant tweets on Dogecoin, which could have come across as noise in the long term. It can be observed that the Musk effect on Dogecoin appeared to sustain before losing momentum and dwindling off since March to 11 April 2021 (Fig 2). These happened in conjunction with the meme-stock frenzy which lasted for the same period.  

Figure 2 : Number of tweets, Price and Vol of Dogecoin, Feb to April 2021

However, these are mainly interpretations as I could not find historical hourly data for dogecoin. Alternatively, trading activities could have been influenced by the Reddit group “SatoshiStreetBets” and “WallStreetBets”. Due to the sudden restrictions from Robinhood on 28th January 2021 following the short squeeze in the stock market, the community turned to a Dogecoin rally given the lack of regulation. Perhaps, Musks’s tweets could have been a reaction, joining the hype after these activities. 









## Analysis on Bitcoin

 
Figure 3 : Overall number of tweets, Price and Vol of Bitcoin Dec 2020 to April 2021

In general, the number of tweets by Elon Musk appeared to have coinciding movements on the volume and price of bitcoin. However, I was particular drawn to the 2 price hikes observed in the months of January and February where the price of Bitcoin appeared to be rather volatile. 

Finding 1 : From 20 December 2020 to 10 January 2021

Upon a detailed analysis on 20th December, it can be seen that the price of Bitcoin tumbled instead and failed to take off  despite Musk’s 2 tweets:  (Figure 4)
•	Bitcoin is my safe word 
•	Bitcoin is almost as bs as fiat money 

Figure 4 : Price and Vol of Bitcoin (8hrs after Musk’s Tweet), 20 Dec 2020 

However, it was Musk’s reactionary comment towards  Microstrategy CEO Saylor   that lead to the price and volume of Bitcoin rose thereafter from 21 December. Saylor had recommended Tesla to buy Bitcoin on Twitter, resulting in a short exchange on Tesla’s potential. These fueled much speculation within the community as institutional and retail investors started purchasing and holding them. The phenomenon resulted in a continuous rise in Bitcoin price and volume. (Figure 4) 

Finding 2 : From 7 February 2021 to 29 February 2021

On 8th February 2021, Tesla announced that it was accepting Bitcoin as a mode of payment , sparking a 10% rise in the price of Bitcoin as trading volume spiked over 3000% in the same day. These were further fueled by Musk’s flurry of tweets over the next 2 weeks, supporting an overall upward trend (Figure 5).

 
Figure 5 : Price and Vol of Bitcoin, 7 Feb 2021 to 29 Feb 2021

Yet, while many claimed that the price drop observed on 21st February was due to Musk’s tweet on 20th February that “BTC.. do seem high”, the trading activity proves otherwise. While it did cause the price of Bitcoin to drop temporarily within 2 hours after the tweet, we observed a further price increase and volume instead for the remaining time and remained above the $55,000 level after 8 hours from the tweet. The price of Bitcoin then hit a new record of $58,042 against a bullish momentum (Figure 6). 

 
Figure 6 : Price and Vol of Bitcoin, 20 Feb 2021


On hindsight, the activities could have been influenced by US Treasury Secretary Janet Yellen’s ominous warnings over Bitcoin on 22nd February 2021 that caused a flight away from the coin. She labelled it as a “speculative asset” and hinted possibilities of a new digital currency during the DealBook DC Policy Project conference . As a result, the price of Bitcoin sharply dropped, dipping to below $46,000 (Figure 7) .

 
Figure 7 : Price and Vol of Bitcoin (Following Yellen’s announcement), 22 Feb 2021


## Discussion 

The study has demonstrated how a culmination of social and political influences can impact the movements in the cryptocurrency markets. In this case, apart from the Musk effect, we see other possible news which could have resulted in the volatile trading volume and prices of these coins. Nevertheless, there are significant events which were a result of Musk’s tweets, more notably how his jokes have circulated on Twitter to impact the price of dogecoin. On the other hand appears to be less susceptible to his tweets unless there were stronger signs of the cryptocurrency from corporate interests of more influential individuals who communicate their opinions on it via social media, creating a stronger market movement. Hence, Musk’s tweets generally acted as a catalyst for the cryptocurrency movements but in some cases, these were reactionary posts as opposed to a constant trigger. 

In this new digital era, it is important to recognize the development of these trading activities are all attributed to the common reason : distributed and participatory nature of Twitter which enabled the autonomous construction of social networks. We witness different segments of society coming together and challenging the traditional notion where only the “big players” control the market. Political actors and news channels can easily amplify messages within this echo chamber, affecting investor sentiments. And of course, Musk, can easily influence his army of 40 million Twitter followers, reminding us that popular online actors can easily disrupt our traditional financial model and distort price signals. 

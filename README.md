# AlphTxnsPerHour
UPenn CIS233 (2022) Final Project

Reifon Chiu, Ruth Chung, Di Lu





The main idea of our project will be to measure the volume of transactions of a (relatively) new cryptocurrency called “Alephium”, which has the ability to have an incredibly high transaction bandwidth of 10,000 transactions per second. Due to this super-high bandwidth, we want to see when transactions tend to occur. This is also unique compared to Bitcoin or Ethereum because of the relative newness of the cryptocurrency, which means that there may be less transactions of larger value, but more transactions overall. The data that we will try to visually represent might be hosted on a website (depending on our ability to create one in time by the due date of the original project) and may be updated live; however, since this is most likely not possible, we decided to stick to some sort of animated showcase of the data.

# Design choices
We initially thought to look at the average number of transactions per hour, but realized that it was a bit of a strange idea, since it isn't actually representative of the current number of transactions, but the number of transactions since the very first transaction on the blockchain. Therefore, we decided to move on to consider the total number of transactions and compare which hour has more transactions compared to others to see if some hours are more popular for transactions than others. One of the major design choices that we made was to exclude block rewards, or mining rewards. This was in an attempt to focus mainly on user transactions instead of mining transactions as well, which was an attempt to get a less inflated visualization of the growth of the Alephium blockchain without needing to worry about the total hashrate or difficulty.


---
## A big thanks to cgi-bin (sven-hash) for his whaleswatcher project here: https://github.com/sven-hash/whaleswatcher.
Some of their code was adapted for this project.
Additionally, the bar-chart-race library was used to make the visual for this project.

---
There are a couple example files included. In the `key.py.example` file, you need to insert your own API key that you create for your own full-node. In the `currTxnTime.txt.example` file, you can insert any time value, but I decided to go with the very start of the day of the first block timestamp of Alephium.

Also, you will need to add `alephium.api.blockflow-fetch-max-age=290000000000` to the full-node configuration file.

The `txnslist.csv.example` file contains all the transactions up `1650650400`, or `Fri Apr 22 2022 14:00:00 GMT-0400 (Eastern Daylight Time)`. Note that I used `1636416000` as my starting time, instead of `1636383298` - the timestamp of the first block. I used `1636416000` because that's the first hour of transactions for Alephium.

# Related Links

https://github.com/alephium 

https://wiki.alephium.org/ 

https://explorer.alephium.org/ 

https://github.com/dexplo/bar_chart_race

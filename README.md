# AlphTxnsPerHour
UPenn CIS233 (2022) Final Project

Reifon Chiu, Ruth Chung, Di Lu


https://user-images.githubusercontent.com/59272129/164774884-0585f252-00e1-43ef-9781-2b43b263ecfb.mp4


# What's this even about?

The main idea of our project will be to measure the volume of transactions of a (relatively) new cryptocurrency called “Alephium”, which has the ability to have an incredibly high transaction bandwidth of 10,000 transactions per second. Due to this super-high bandwidth, we want to see when transactions tend to occur. This is also unique compared to Bitcoin or Ethereum because of the relative newness of the cryptocurrency, which means that there may be less transactions of larger value, but more transactions overall. The data that we will try to visually represent might be hosted on a website (depending on our ability to create one in time by the due date of the original project) and may be updated live; however, since this is most likely not possible, we decided to stick to some sort of animated showcase of the data.

# Design Choices
We initially thought to look at the average number of transactions per hour, but realized that it was a bit of a strange idea, since it isn't actually representative of the current number of transactions, but the number of transactions since the very first transaction on the blockchain. Therefore, we decided to move on to consider the total number of transactions and compare which hour has more transactions compared to others to see if some hours are more popular for transactions than others. One of the major design choices that we made was to exclude block rewards, or mining rewards. This was in an attempt to focus mainly on user transactions instead of mining transactions as well, which was an attempt to get a less inflated visualization of the growth of the Alephium blockchain without needing to worry about the total hashrate or difficulty.

# Walking Through the Code
The code is focused into 3 sections: Collecting data, Parsing the data, and then Graphing the data.

## Collecting the data
### Some precursory thoughts: 
We decided that in order to collect the data, it would be best to grab the data directly from the blockchain and parse through it. Not only does this help us figure out how to work with the blockchain, but it also helps the blockchain as it requires us to run our own full-node. In short, running a full-node helps with the security of the blockchain, but you can read more in the wiki, or ask in the Alephium Discord server. We also decided that webscraping from the explorer would not be a good solution due to the short-term lifespan of a webscraping approach. Instead, our approach is more focused on the longevity and the ability to reproduce the visuals for oneself, instead of having to rely on provided data (like the ones we give in the `.example` files). Furthermore, we figured that this would also encourage people to run their own full-nodes so they have it set up for their own projects. Also, a quick heads up about running your own full-node: it takes up 15+ gbs as of April, 2022, and may take over an hour to verify the entire blockchain up to the current time.

### The technical parts
First off, we decided to store the transactions list in `txnslist.csv`, and we kept track of the time that we left off on, so that if the program is rerun, it can continue off of the existing values. That being said, it doesn't hurt to reset the `txnslist.csv` file every once in a while if you need to start from the beginning of the blockchain, but please read the comments at the top of `main.py` for how to properly do that. The general idea is this: We begin at a certain timestamp (which is stored in `currTxnTime.txt`), and we read the data from the blockchain for the 60 minutes (3600 seconds) before that timestamp. From the blockchain (notice that it's an API call to the locally hosted full-node), we get a series of responses, and in the case that we're focused on, we get all the way into the specific block, and for each transaction in the block, we increment our `txs` counter per each transaction that has more than 1 input to the transaction. This is the code that allows us to exclude transactions that are block/mining rewards (block/mining rewards have no inputs to the trasactions, and those transactions are the payouts for mining the block). In any case that there's an error, we return `-1`, and break out of the collection. However, if that's not the case, then we continue on, and write the number of transactions for the hour leading up to the timestamp, and the timestamp next to it in the csv. This process can end up taking a while. The longer the blockchain, the longer it'll take, but as of April 2022, it took around 5 mins or so for this part of the program to finish.

## Parsing the data
This part and the next one are both in `parseData.py`. The main focus of parsing the data was to format the data in `txnslist.csv` to something usable by the `bar-chart-race` library (linked in the code and below in Related Links.) The main datastructure here was just the dict `hours` that stores the total transactions that happened each hour, and as we read each line in `txnslist.csv`, we update `hours`. Then, each time there is a new day, we write to `fdata.csv`. That's it.

## Creating the graph
Here we just format the input for the `bar-chart-race` library and wait for the output to be rendered as `visualizedTxData.mp4`. This took around 5-10 minutes for the program to finish.

---

## Working on this yourself
If you are interested in figuring out how to use this program as well, there's good news! The `.example` files are the exact same as the non `.example` files. Therefore, all you have to do is remove the `.example` extension on the files, and you're almost ready to go. A couple things to note: you need to set up your own local full-node. A guide for that can be found in the Alephium wiki (in Related Links below). As I stated above, it can take a while to validate the blocks until things are up to date, but once you have that set up, then you are *almost* ready. **Make sure you set the `X-API-key` in the `key.py` file**. Once you've done that, you should be good to go! Just keep in mind that running this for the first time can take quite a while, but there are somethings printed out to the console to let you know what step the program is in. The only exception is the graph creation process, which takes a long time, but I can't do anything about that since the person who made it didn't accept the merge request to add a progress bar.

---
## A big thanks to cgi-bin (sven-hash) and his whaleswatcher project here: https://github.com/sven-hash/whaleswatcher.
Some of their code was adapted for this project.
Additionally, the `bar-chart-race` library was used to make the visual for this project.

---
## Other notes
There are a couple example files included. In the `key.py.example` file, you need to insert your own API key that you create for your own full-node. In the `currTxnTime.txt.example` file, you can insert any time value, but I decided to go with the very start of the day of the first block timestamp of Alephium.

Also, you will need to add `alephium.api.blockflow-fetch-max-age=290000000000` to the full-node configuration file.

The `txnslist.csv.example` file contains all the transactions up `1650650400`, or `Fri Apr 22 2022 14:00:00 GMT-0400 (Eastern Daylight Time)`. Note that I used `1636416000` as my starting time, instead of `1636383298` - the timestamp of the first block. I used `1636416000` because that's the first hour of transactions for Alephium.

# Related Links
https://alephium.org/ 

https://github.com/alephium 

https://wiki.alephium.org/ 

https://explorer.alephium.org/ 

https://github.com/dexplo/bar_chart_race 

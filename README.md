# AlphTxnsPerHour
UPenn CIS233 (2022) Final Project

Reifon Chiu, Ruth Chung, Di Lu


https://user-images.githubusercontent.com/59272129/164610653-d1175fc2-4209-4d74-8773-936ebf9eb914.mp4


The main idea of our project will be to measure the volume of transactions of a (relatively) new cryptocurrency called “Alephium”, which has the ability to have an incredibly high transaction bandwidth of 10,000 transactions per second. Due to this super-high bandwidth, we want to see when transactions tend to occur. This is also unique compared to Bitcoin or Ethereum because of the relative newness of the cryptocurrency, which means that there may be less transactions of larger value, but more transactions overall. The data that we will try to visually represent might be hosted on a website (depending on our ability to create one in time) and may be updated live; however, in the case that it is not possible, we might just stick to still images, or a file that will run and locally display the data as it updates live. This tool will be helpful in understanding whether our hypothesis about how Alephium is being used currently is correct. If we have more time, we can also attempt to examine the top used dApps and output those as well.

---
## A big thanks to cgi-bin (sven-hash) for his whaleswatcher project here: https://github.com/sven-hash/whaleswatcher.
Some of their code was adapted for this project.
Additionally, the bar-chart-race library was used to make the visual for this project.

---
There are a couple example files included. In the `key.py.example` file, you need to insert your own API key that you create for your own full-node. In the `currTxnTime.txt.example` file, you can insert any time value, but I decided to go with the very start of the day of the first block timestamp of Alephium.

Also, you will need to add `alephium.api.blockflow-fetch-max-age=290000000000` to the full-node configuration file.

The `txnslist.csv.example` file contains all the transactions up `1650603600`, or `Fri Apr 22 2022 01:00:00 GMT-0400 (Eastern Daylight Time)`. Note that I used `1636416000` as my starting time, instead of `1636383298` - the timestamp of the first block. I used `1636416000` because that's the first hour of transactions for Alephium.

# Related Links

https://github.com/alephium 

https://wiki.alephium.org/ 

https://explorer.alephium.org/ 

https://github.com/dexplo/bar_chart_race

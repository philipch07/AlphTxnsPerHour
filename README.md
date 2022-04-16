# AlphTxnsPerHour
UPenn CIS233 (2022) Final Project

Reifon Chiu, Ruth Chung, Di Lu

The main idea of our project will be to measure the volume of transactions of a (relatively) new cryptocurrency called “Alephium”, which has the ability to have an incredibly high transaction bandwidth of 10,000 transactions per second. Due to this super-high bandwidth, we want to see when transactions tend to occur. This is also unique compared to Bitcoin or Ethereum because of the relative newness of the cryptocurrency, which means that there may be less transactions of larger value, but more transactions overall. The data that we will try to visually represent might be hosted on a website (depending on our ability to create one in time) and may be updated live; however, in the case that it is not possible, we might just stick to still images, or a file that will run and locally display the data as it updates live. This tool will be helpful in understanding whether our hypothesis about how Alephium is being used currently is correct. If we have more time, we can also attempt to examine the top used dApps and output those as well.

---
## A big thanks to cgi-bin (sven-hash) for his whaleswatcher project here: https://github.com/sven-hash/whaleswatcher.
Some of their code was adapted for this project.

---
There are a couple example files included. In the `key.py.example` file, you need to insert your own API key that you create for your own full-node. In the `currTxnTime.txt.example` file, you can insert any time value, but I decided to go with the very start of the day of the first block timestamp of Alephium.

Also, you will need to add `alephium.api.blockflow-fetch-max-age=290000000000` to the full-node configuration file.

# Related Links

https://github.com/alephium 

https://wiki.alephium.org/ 

https://explorer.alephium.org/ 
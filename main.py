from datetime import datetime, timedelta
from key import header
import requests

API_BASE = "http://127.0.0.1:12973"
API_EXPLORER_BASE = "https://mainnet-backend.alephium.org"
ALPH = '\u2135'
#GENESIS_TS = 1231006504
#FIRST_BLOCK_TS = 1636383298
#############################
#MY_STARTING_TS = 1636347600#
#############################

# gets the transactions from the user's own full-node (see API_BASE)
def getBlockTsTransactions(session, start, end):
    txs = 0
    response = session.get(f"{API_BASE}/blockflow?fromTs={start * 1000}&toTs={end * 1000}")

    allBlocks = response.json()
    # this thing doesn't work yet; getting error code 400 (bad input)
    for inBlock in allBlocks['blocks']:
        for block in inBlock:
            for transaction in block['transactions']:
                if len(transaction['unsigned']['inputs']) > 0:
                    txs += 1
    # return transaction array
    return txs

def tconv(a):
    return int(datetime.timestamp(a))

def main():
    # start where we leave off
    f = open("currTxnTime.txt", "r+")
    # we store the txns and the time here
    vals = open("txns_list.csv", "a")

    # gets the number of txns in the past hour and stores it in the csv
    # also updates the time in the starting file currTxnTime.txt
    while (int(f.read()) < tconv(datetime.now())):
        f.seek(0)
        currTime = int(f.read())
        # creating a request session
        s = requests.Session()
        s.headers.update(header)

        numTxs = getBlockTsTransactions(s, tconv(datetime.fromtimestamp(currTime) - timedelta(hours=1)), tconv(datetime.now()))
        vals.write(numTxs, currTime)
        print(numTxs, currTime)
        f.write(currTime + timedelta(hours=1))

if __name__ == "__main__":
    main()

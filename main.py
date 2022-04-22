from datetime import datetime, timedelta
from key import header
from parseData import parse, graph
import requests

API_BASE = "http://127.0.0.1:12973"
a = '\u2135'
# Just a heads up that if you need to clear the txnslist.csv file, set it to be:
"""
txn,timeutc

"""
# including the newline.

# GENESIS_TS = 1231006504
# FIRST_BLOCK_TS = 1636383298
###############################
# MY_STARTING_TS = 1636416000 #
###############################

# gets the transactions from the user's own full-node (see API_BASE)
def getBlockTsTransactions(session, start, end):
    txs = 0
    # multiplying by 1000 to convert s (unix ts) to ms
    response = session.get(f"{API_BASE}/blockflow?fromTs={start * 1000}&toTs={end * 1000}")

    allBlocks = response.json()
    if (response.ok) :
        for inBlock in allBlocks['blocks']:
            for block in inBlock:
                for transaction in block['transactions']:
                    if len(transaction['unsigned']['inputs']) > 0:  # this filters out block rewards, which have no inputs
                        txs += 1
    else:
        print(f"There was an error code. See error: {response.status_code}")
        return -1

    # return number of transactions
    return txs

def tconv(a):
    return int(datetime.timestamp(a))

def collect():
    print("Collecting data...")
    # This logic helps us to continue where we left off.
    f = open("currTxnTime.txt", "r+")
    # Storing the txns and the time in txnslist.csv
    vals = open("txnslist.csv", "a")

    # Gets the number of txns in the past hour and stores it in the csv
    # Also updates the time in the starting file currTxnTime.txt
    # I use a try-except block to catch the ctrl+c so it terminates cleanly.
    # Also note the f.seek(0) are necessary to keep the file line pointer at the top of the file.
    try:
        while (int(f.read()) < tconv(datetime.now())):
            f.seek(0)
            currTime = int(f.read())

            s = requests.Session()
            s.headers.update(header)

            # getting the number of transactions
            # returns -1 on error status code
            numTxs = getBlockTsTransactions(s, currTime - 3600, currTime)
            if (numTxs == -1):
                return

            vals.write(f'{numTxs},{currTime}\n')
            print(f'{numTxs}, {datetime.fromtimestamp(currTime).strftime("%m/%d/%Y, %H")}')
            newTime = currTime + 3600
            f.seek(0)
            f.write(str(newTime))
            f.seek(0)

        print(f'\n{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}')
        print("All Caught Up!")
        print(f'{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}{a}')
        print("\nData collected.\n")
    except KeyboardInterrupt:
        print('Interrupted. Terminating collection.')

    f.close()
    vals.close()

def main():
    collect()
    parse()
    graph()

if __name__ == "__main__":
    main()

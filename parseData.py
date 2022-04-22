import csv
from datetime import datetime
import bar_chart_race as bcr
import pandas as pd

# Parses the data in the csv into dicts and stores them into another csv
# Note that this won't continue off of anywhere, and will have to parse through txnslist.csv from the very beginning.
# This shouldn't be much of an issue though, as this part runs much quicker than the first part.
def parse():
    print("Parsing data...")
    # The format of hours and months is:
    # {
    #   { hr/mo,
    #     { totaltxns,
    #       count,
    #       average
    #     }
    #   }, ...
    # }
    hours = {}
    # this `tot` variable was just to check how many total transactions have been made.
    # tot = 0

    for i in range(0, 24):
        #hours[i] = {"totalTxns": 0, "count": 0, "average": 0}
        hours[i] = {"totalTxns": 0}

    with open ('txnslist.csv', newline = '\n') as c:
        r = csv.DictReader(c)
        fdata = open("fdata.csv", "w")
        fdata.write("date,0-1,1-2,2-3,3-4,4-5,5-6,6-7,7-8,8-9,9-10,10-11,11-12,12-13,13-14,14-15,15-16,16-17,17-18,18-19,19-20,20-21,21-22,22-23,23-0\n")
        for row in r:
            txn = int(row["txn"])
            ts = int(row["timeutc"])
            date = datetime.fromtimestamp(ts)

            # deciding when to write to fdata.csv
            # only write on midnights (hour is 0), specifically for formatting the .csv in a better way for the racing bar graph.
            if date.hour == 0:
                fdata.write(f'{date.strftime("%m/%d/%Y")},')
                for i in range(1, 24):
                    # fdata.write(f'{hours[i]["average"]},')
                    fdata.write(f'{hours[i]["totalTxns"]},')
                # fdata.write(f'{hours[0]["average"]}\n')
                fdata.write(f'{hours[0]["totalTxns"]}\n')

            hours[date.hour]["totalTxns"] += txn
            # tot += txn
            # hours[date.hour]["count"] += 1
            # hours[date.hour]["average"] = round(hours[date.hour]["totalTxns"] / hours[date.hour]["count"], 2)

    print("Parsing finished!")
    # print(f'Total Transactions: {tot}')

# Creates the .mp4 animated bar chart race
def graph():
    print("Creating graph...")
    # https://github.com/dexplo/bar_chart_race
    tot = 0
    df = pd.read_csv('fdata.csv', index_col = 'date', parse_dates=['date'])
    df.tail()
    bcr.bar_chart_race(
        df = df,
        filename = 'visualizedTxData.mp4',
        orientation = 'h',
        sort = 'desc',
        n_bars = 24,
        fixed_order = ["0-1","1-2","2-3","3-4","4-5","5-6","6-7","7-8","8-9","9-10","10-11","11-12","12-13","13-14","14-15","15-16","16-17","17-18","18-19","19-20","20-21","21-22","22-23","23-0"],
        fixed_max = False,
        steps_per_period = 30,
        period_length = 500,
        end_period_pause = 10,
        interpolate_period = False,
        period_label = {'x': .98, 'y': .4, 'ha': 'right', 'va': 'center'},
        period_template = '%B %d, %Y',
        period_summary_func = lambda v, r:{'x': .98, 'y': .3,
                                        's': f'Total tx\'s: {v.sum():,.0f}',
                                        'ha': 'right', 'size': 10},
        perpendicular_bar_func = None,
        colors = 'dark24',
        title = 'Total Transactions Per Hour on the Alephium Blockchain (UTC-4)',
        bar_size = .95,
        bar_textposition = 'inside',
        bar_texttemplate='{x:,.0f}', 
        bar_label_font=7, 
        tick_label_font=8, 
        tick_template='{x:,.0f}',
        shared_fontdict=None, 
        scale='linear', 
        fig=None, 
        writer=None, 
        bar_kwargs={'alpha': .7},
        fig_kwargs={'figsize': (6, 3.5), 'dpi': 144},
        filter_column_colors=False
    )

    print("The graph has been made!")

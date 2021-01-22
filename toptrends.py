import argparse
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Display top trends during a year. ')
parser.add_argument('--year', type=int, default=2020, help='year of top trends')
parser.add_argument('--language', type=str, default='en', help='language of search term (en, en-US, en-GB, de, ...)')
parser.add_argument('--region', type=str, default='GLOBAL', help='country-province/state (GLOBAL, CH, US-AL, ...)')

if __name__ == '__main__':
    args = parser.parse_args()

    pytrend = TrendReq()

    df = pytrend.top_charts(args.year, hl=args.language, tz=0, geo=args.region)

    # get time series and calculate date of max interest
    dataframes = []
    for title in list(df['title'].values):
        pytrend.build_payload(
            kw_list=[title],
            timeframe='all')
        data = pytrend.interest_over_time()
        data = data.drop(labels=['isPartial'], axis='columns')
        dataframes.append(data.loc[str(args.year) + '-01-01':str(args.year + 1) + '-01-01'])

    # sort by date of max popularity
    dataframes = sorted(dataframes, key=lambda x: x[x.values == x.values.max()].index)

    # make plot
    fig, ax = plt.subplots(nrows=len(df['title'].values), ncols=2, figsize=(8, 6), gridspec_kw={'width_ratios': [1, 3]})
    for row, dataframe in enumerate(dataframes):
        dataframe.plot.area(ax=ax[row, 1], legend=False)
        ax[row, 0].text(0, 0.25, dataframe.columns[0], fontsize=12)
        ax[row, 0].axis(False)
        ax[row, 1].spines['top'].set_visible(False)
        ax[row, 1].spines['right'].set_visible(False)
        ax[row, 1].spines['bottom'].set_visible(False)
        ax[row, 1].spines['left'].set_visible(False)
        ax[row, 1].axes.yaxis.set_visible(False)
        # ax[row, 1].grid(True, axis='x', which='both')
        if row != (len(dataframes) - 1):
            ax[row, 1].axes.xaxis.set_visible(False)
            ax[row, 1].tick_params(axis='both', which='both', length=0)
            plt.setp(ax[row, 1], xticks=[], xticklabels=[], yticks=[])

    plt.suptitle('Relative Search Interest of Top 10 Google Searches {} in {}'.format(str(args.year), args.region))
    fig.subplots_adjust(hspace=0, wspace=0.3)
    plt.xlabel('')
    plt.show()
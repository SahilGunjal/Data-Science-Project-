import yfinance as yf
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt


def read_data_library():
    apple = yf.Ticker("AAPL")

    # Getting apple information
    # apple_info = apple.info

    # getting apple stock prizes since beginning
    apple_share_price_data = apple.history(period="max")
    return apple_share_price_data


def read_data_scrapping():
    # currently issue at their end
    url = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'
    data = requests.get(url).text
    soup = BeautifulSoup(data,'html.parser')

    tables = soup.find_all('table')
    print(len(tables))
    print(tables)
    dataframe_scrapping = pd.read_html(str(tables[0]))
    print(dataframe_scrapping)


def main():
    # reading the data from python library yfinance
    df_l = read_data_library()
    print(len(df_l))

    # reading the data by web scrapping
    # df_s = read_data_scrapping()

    print(df_l.iloc[,])
    # plt.hist(df_l.iloc[:,0])


if __name__ == "__main__":
    main()
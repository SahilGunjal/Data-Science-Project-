from bs4 import BeautifulSoup
import requests
import pandas as pd


def main():
    url = 'https://en.wikipedia.org/wiki/World_population'
    data = requests.get(url).text

    soup = BeautifulSoup(data,'html.parser')
    table = soup.find('table')
    df = pd.read_html(str(table))
    print(df)


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
import requests
import sys
from bs4 import BeautifulSoup
import time
import cProfile
import pstats


def fetch_financial_data(ticker, field):

    ticker = ticker.lower()

    url = f"https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching data: {e}")

    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find("div", {"class": "tableBody"})
    
    if not table:
        raise Exception(f"Financial data for ticker '{ticker}' not found.")

    rows = table.find_all("div", {"class": "row"})
    
    for row in rows:
        if field.lower() in row.text.lower():
            cols = row.find_all("div")
            values = [col.text.strip() for col in cols[1:] if col.text.strip()]
            return tuple(values)

    raise Exception(f"Field '{field}' not found for ticker '{ticker}'.")


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: ./financial.py 'TICKER' 'FIELD'")
        sys.exit(1)

    ticker = sys.argv[1]
    field = sys.argv[2]

    try:
        pr = cProfile.Profile()
        pr.enable()

        data = fetch_financial_data(ticker, field)
        print(data)
        
        pr.disable()

        with open("pstats-cumulative.txt", "w") as f:
            ps = pstats.Stats(pr, stream=f)
            ps.sort_stats('cumulative').print_stats(5)
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

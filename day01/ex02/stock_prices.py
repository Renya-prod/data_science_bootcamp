import sys

def get_stock_price():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    if len(sys.argv) != 2:
        return
     
    input_name = sys.argv[1].lower()
    companies_lower = {}
    for key, value in COMPANIES.items():
        companies_lower[key.lower()] = value

    if input_name in companies_lower:
        stock_symbol = companies_lower[input_name]
        stock_price = STOCKS.get(stock_symbol, "Unknown stock")
        print(stock_price)
    else:
        print("Unknown company")

if __name__ == '__main__':
    get_stock_price()
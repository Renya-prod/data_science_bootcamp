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
     
    input_name = sys.argv[1].upper()
    companies_upper = {}
    for key, value in COMPANIES.items():
        companies_upper[value] = key

    if input_name in companies_upper:
        company_name = companies_upper.get(input_name, "Unknown company")
        stock_price = STOCKS[input_name]
        print(f"{company_name} {stock_price}")
    else:
        print("Unknown company")

if __name__ == '__main__':
    get_stock_price()
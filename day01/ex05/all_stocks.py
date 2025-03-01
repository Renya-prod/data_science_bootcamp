import sys

def process_stocks():
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

    input_string = sys.argv[1]
    
    expressions = [expr.strip() for expr in input_string.split(',')]

    if '' in expressions:
        return
    
    companies_lower = {key.lower(): value for key, value in COMPANIES.items()}
    tickers_to_companies = {value: key for key, value in COMPANIES.items()}

    for expr in expressions:
        expr_lower = expr.lower()
        expr_upper = expr.upper()

        if expr_lower in companies_lower:
            stock_symbol = companies_lower[expr_lower]
            stock_price = STOCKS.get(stock_symbol, "Unknown stock")
            print(f"{expr_lower.capitalize()} stock price is {stock_price}")
        elif expr_upper in tickers_to_companies:
            company_name = tickers_to_companies.get(expr_upper, "Unknown company")
            stock_price = STOCKS.get(expr_upper, "Unknown stock")
            print(f"{expr_upper} is a ticker symbol for {company_name}")
        else:
            print(f"{expr} is an unknown company or an unknown ticker symbol")

if __name__ == '__main__':
    process_stocks()
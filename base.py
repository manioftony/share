import yfinance as yf




pfe = yf.Ticker('HUDCO.NS')
# pfe.info
hist = pfe.history(period='6mo')

# print (hist.info())
# df1 = hist[['Open']]
# print(df1)

stock_52w_change = []
profitsMargins = []
tickers = ['HUDCO.NS','IRFC.NS']
for ticker in tickers:
    print(ticker)
    current_ticker = yf.Ticker(ticker)
    current_ticker_info = current_ticker.info
    stock_52w_change.append(current_ticker_info['currentPrice'])
    # profitsMargins.append(current_ticker_info['profitMargins'])
print (stock_52w_change)
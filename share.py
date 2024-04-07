import yfinance as yf
tickers = ['HUDCO.NS','IRFC.NS','LOYALTEX(NSE)']
for ticker in tickers:
    # data = yf.download(ticker, start="2024-03-18", end="2024-03-20")
    recent_data = yf.download(ticker, period="5d")
    print(recent_data)
    # print(data.head())
from flask import Flask, render_template, request, redirect, url_for, g, jsonify, session
import yfinance as yf


app = Flask(__name__)

def get_current_price(data):
    try : 
        if data == 'empty':
            return data
        else:
            # data = data.replace('(NSE)','')+'.NS'
            current_ticker = yf.Ticker(data)
            current_ticker_info = current_ticker.info
            data = current_ticker_info['currentPrice']
            return data
    except:
        return 'empty'



@app.route('/', methods=['POST', 'GET', 'PUT'])
def index():
    username = "HUDCO.NS"
    liveprice = get_current_price(username) 
    data = yf.download("HUDCO.NS", start="2024-03-01", end="2024-04-07")
    data['total'] = data['High']-data['Open']
    # data['total1'] = data['Low']-data['Open']
    data['status'] = data['total']>=4
    # data = data[data['status']== False]
    date = list(data.index.astype(str))
    data = list(data['total'])

    # print (date,data)
    if request.method == 'POST':
        username = request.form['username']
        username = username.upper()+".NS"
        liveprice = get_current_price(username) 
        data = yf.download(username, start="2024-01-01", end="2024-04-07")
        data['total'] = data['High']-data['Open']
        # data['total'] = data['Low']-data['Open']
        data['status'] = data['total']>=4
        # data = data[data['status']== False]
        count = data.count()[0]
        date = list(data.index.astype(str))
        data = list(data['total'])

        # import ipdb;ipdb.set_trace()
        return render_template('index.html', **locals())
    else:
        return render_template('index.html', **locals())




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)

    # app.run(debug=True)
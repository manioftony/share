import requests
from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd
import bs4
import yfinance as yf


def nsename(text):
    try : 
        url = 'https://google.com/search?q=' + text
        request_result = requests.get(url)
        soup = bs4.BeautifulSoup(request_result.text, "html.parser")
        heading_object = soup.find_all('span')
        data = []
        for info in heading_object:
            if 'NSE' in info.getText():
                data.append(info.getText())
        return data[0]
    except:
        return 'empty'

def get_current_price(data):
    try : 
        if data == 'empty':
            return data
        else:
            data = data.replace('(NSE)','')+'.NS'
            current_ticker = yf.Ticker(data)
            current_ticker_info = current_ticker.info
            data = current_ticker_info['currentPrice']
            return data
    except:
        return 'empty'

def is_positive(value):
    if value > 0:
        return True
    else:
        return False

url = "https://munafasutra.com/nse/top/GAINERS/Day/2"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'lxml')

# Convert BeautifulSoup object to lxml object
xml_content = etree.HTML(str(soup))

# Use XPath to select the table element
table_elements = xml_content.xpath("/html/body/div[2]/div/div[5]/div[1]/table")

# Initialize a list to store data
data = []

# Iterate over table elements
for table_element in table_elements:
    # Iterate over rows skipping the header row
    for row in table_element.xpath(".//tr")[1:]:
        # Extract data from each cell of the row
        cells = row.xpath(".//td//text()")
        company = cells[1].strip()
        change_percent = cells[3].strip()
        current_price_value = cells[4].strip()
        last_2_days_price = cells[5].strip()
        company = company + ' share price'
        nse = nsename(company)
        liveprice = get_current_price(nse) 
        # print ('1=' ,nse)
        # print ('2=' ,current_price_value)
        # print ('3=' ,liveprice)

        # print ('===status===',nse=='empty' and liveprice=='empty')


        if nse=='empty' and liveprice=='empty':
            total = nse
        elif nse!='empty' and liveprice=='empty':
            total = nse
        else:
            total = float(current_price_value) - float(liveprice)
            status = is_positive(total)
        # Append data to the list
        data.append({
            'nse':nse,
            'Company': company,
            'Change Percent': change_percent,
            'Current Price': current_price_value,
            'Last 2 Days Price': last_2_days_price,
            'liveprice': liveprice,
            'total':total,
            'status':status
        })

# Convert data to a DataFrame
df = pd.DataFrame(data)
# import ipdb;ipdb.set_trace()
# Print the DataFrame

from datetime import datetime

now = datetime.now()
# name = now.strftime("%d_%m_%Y_%H_%M_%S")
name = now.strftime("%d_%m_%Y_%H_%M_%S")+'.csv'
df.to_csv("result/"+name)
print(df)

obj = df.groupby('status').count()
name = now.strftime("%d_%m_%Y_%H_%M_%S_status")+'.csv'
obj.to_csv("result/"+name)
print (obj)




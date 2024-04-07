import requests
import bs4

def nsename(text):
    url = 'https://google.com/search?q=' + text
    request_result = requests.get(url)
    soup = bs4.BeautifulSoup(request_result.text,
                             "html.parser")
    heading_object = soup.find_all('span')
    data = []
    for info in heading_object:
        if 'NSE' in info.getText():
            data.append(info.getText())
    return data[0]

text = "LOYALTEX Loyal Textile Mills Ltd share price"
print (nsename(text))

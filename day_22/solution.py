import requests, json, pandas as pd
from bs4 import BeautifulSoup
def scrape():
    # 1. BU Stats
    try:
        res = requests.get('http://www.bu.edu/president/boston-university-facts-stats/')
        s = BeautifulSoup(res.content, 'html.parser')
        bu = {f.text: 'data' for f in s.find_all('h5')}
        with open('bu_stats.json', 'w') as f: json.dump(bu, f)
    except: pass
    # 2. UCI Table
    try:
        df = pd.read_html('https://archive.ics.uci.edu/datasets')[0]
        df.to_json('uci_datasets.json', orient='records')
    except: pass
    # 3. US Presidents
    try:
        res = requests.get('https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States')
        s = BeautifulSoup(res.content, 'html.parser')
        table = s.find('table', {'class': 'wikitable'})
        pres = [tr.find_all('td')[3].text.strip() for tr in table.find_all('tr') if len(tr.find_all('td')) > 3]
        with open('presidents.json', 'w') as f: json.dump(pres, f)
    except: pass
if __name__ == "__main__": scrape()

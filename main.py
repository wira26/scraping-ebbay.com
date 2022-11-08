import os
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.ebay.com/sch/i.html?'
params = {
    "_from": 'R40',
    "_trksid": 'p2334524.m570.l1313',
    "_nkw": 'smartphone',
    "_sacat": '0',
}
2
result = []


r = requests.get(url, params=params)

soup = BeautifulSoup(r.content, 'html.parser')

contents = soup.find_all('li', {'class':'s-item s-item__pl-on-bottom'})

for i in contents:
    title = i.find('div', {'class':'s-item__title'}).text
    try:
        price = i.find('span', {'class':'s-item__price'}).text
    except:
        continue
    try:
        locations = i.find('span', {'class':'s-item__location'}).text
    except:
        continue
    try:
        review = i.find('div', {'class':'s-item__reviews'}).text
    except:
        review = 'no review'
    
    
    data_dict = {
        'title':title,
        'price':price,
        'locations':locations,
        'review':review
    }

    result.append(data_dict)
# WRITE JSON
with open('json_result.json', 'w') as outfile:
    json.dump(result, outfile)
# READ JSON
with open('json_result.json') as json_file:
    data_dict = json.load(json_file)

    for i in data_dict:
        print(i)

    df = pd.DataFrame(data_dict)
    df.to_csv('result.csv', index=False)
    df.to_excel('result.xlsx', index=False)
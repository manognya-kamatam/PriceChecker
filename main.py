import json

import requests

st = ''
with open(".file") as s:
    st = st.read()


params = {
    'api_key': '25D582A47BE04CB9BA5FBD93890254B7',
    'type': 'search',
    'amazon_domain': 'amazon.com',
    'search_term': st
}

# make the http GET request to Rainforest API
api_result = requests.get('https://api.rainforestapi.com/request', params)

# print the JSON response from Rainforest API
file = json.dumps(api_result.json())

f = open("data.json", "w+")
f.write(file)
f.close()


with open('data.json') as g:
    d = json.load(g)

searchresults = d["search_results"]

prices = []
links = []
names = []
for p in range(len(searchresults)):
    products = searchresults[p]
    print(products)
    if 'price' in products:
        if 'link' in products:
            price = products['price']
            prices.append(price['value'])

            link = products['link']
            links.append(link)

            name = products['title']
            names.append(name)


data = {
  'price': prices,
  'link': links,
  'name': names
}

FilteredData = json.dumps(data)
FD = open("FD.json", "w+")
FD.write(FilteredData)
f.close()

import json
import requests

st = ''
with open(".file") as s:
     st = s.read()

params = {
    'api_key': '273CE7DCC4D24B6DAD61183544F449C3',
    'type': 'search',
    'search_term': st,
    'sort_by': 'best_match'
}

# make the http GET request to BlueCart API
api_result = requests.get('https://api.bluecartapi.com/request', params)

# store the JSON response from BlueCart API
file = json.dumps(api_result.json())

# f = open("data.json", "w+")
# f.write(file)
# f.close()

# load file into a dict in a variable
d = json.loads(file)

# getting only search results
SearchResults = d['search_results']

walprice = 5
products = SearchResults[0]
if 'price' in products['offers']['primary']:
    walprice = products['offers']['primary']['price']

else:
    walprice = "No Price Available"

walname = products['product']['title']
wallink = products['product']['link']

DWal = {
  'name': walname,
  'price': walprice,
  'link': wallink
}





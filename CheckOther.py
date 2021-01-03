import json
import requests

st = 'lamp'
# with open(".file") as s:
#      st = s.read()

params = {
    'api_key': '273CE7DCC4D24B6DAD61183544F449C3',
    'type': 'search',
    'search_term': st,
    'sort_by': 'best_match'
}


api_result = requests.get('https://api.bluecartapi.com/request', params)


file = json.dumps(api_result.json())

d = json.loads(file)


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

Dwalj = json.dumps(DWal)

w = open("wdata.json", "w+")
w.write(Dwalj)
w.close()


url = "https://target-com-store-product-reviews-locations-data.p.rapidapi.com/product/search"

querystring = {"store_id":"3991","keyword":st,"sponsored":"1","limit":"50","offset":"0"}

headers = {
    'x-rapidapi-key': "e39bdaad74mshf9264caaaca51e9p103e55jsna3454bec5cb6",
    'x-rapidapi-host': "target-com-store-product-reviews-locations-data.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
Tfile = json.dumps(response.json())



Td = json.loads(Tfile)

price = Td["products"][0]['price']


tprice = 0

tname = Td["products"][0]["title"]

if price["is_current_price_range"]:
    tprice = price["current_retail_min"]
else:
    tprice = price["current_retail"]

tdata = {
    "name": tname,
    "price": tprice
}

tdataj = json.dumps(tdata)
t = open("tdata.json","w+")
t.write(tdataj)
t.close()











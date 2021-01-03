import json

import requests

# Reading the File with the search term User entered
st = ''
# with open(".file") as s:
#     st = s.read()


params = {
    'api_key': '25D582A47BE04CB9BA5FBD93890254B7',
    'type': 'search',
    'amazon_domain': 'amazon.com',
    'search_term': st,
    'sort_by': 'featured'
}

# make the http GET request to Rainforest API
api_result = requests.get('https://api.rainforestapi.com/request', params)

# store the JSON response from Rainforest API
file = json.dumps(api_result.json())


d = json.loads(file)

# storing only the Search Results
searchresults = d["search_results"]

# making arrays for all values needed from search results
prices = []
links = []
names = []

# getting values needed and storing in arrays
for p in range(len(searchresults)):
    products = searchresults[p]

    if 'price' in products:
        if 'link' in products:
            price = products['price']
            prices.append(price['value'])

            link = products['link']
            links.append(link)

            name = products['title']
            names.append(name)

data = {
    'name': names,
    'price': prices,
    'link': links

}

FilteredData = json.dumps(data)
FD = open("FD.json", "w+")
FD.write(FilteredData)
FD.close()

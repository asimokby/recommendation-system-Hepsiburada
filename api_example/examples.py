import requests
import json
from helpers import show_products_info


# displaying the product's info (which is the product that is in the cart)
print('#'*10, 'Input Product', '#'*10)
show_products_info(['ZYBICN9286868'], with_sims=False)

# sending a post request to the server 
data = {'product_id': 'ZYBICN9286868'} 
response = requests.post("http://127.0.0.1:5000/get_related_products", json.dumps(data))


# receiving the response and displaying the recommended products in the terminal
res = json.loads(response.content)
print('#'*10, 'Recommended Products', '#'*10)
show_products_info(res['ids'], res['sims'])

# displaying the response status 
print('#'*10, 'Response Status', '#'*10)
print(response.status_code, response.reason)


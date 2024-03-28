import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/products')
    print(r.status_code)
    #print(r.text)
    #print(type(r.text))
    categories = r.json()
    #print(categories)
       
    for category in categories:
        print(category['category']['name'])
        #print(category['name']) -> esto genera error


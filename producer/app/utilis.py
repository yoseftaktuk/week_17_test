import json



def save_file():
    with open('data/suspicious_customers_orders.json') as f:
        data = json.load(f)
        return data
 

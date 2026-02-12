import json



def save_file():
    with open('data/suspicious_customers_orders.json') as f:
        data = json.load(f)
        filtered_data = [
        item for item in data
        if item.get('customerNumber')
    ]

    return filtered_data
 

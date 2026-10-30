customer_id = "C001"
customer_name = "Amit Sharma"
city = "Pune"
balance = 125000.50

print(f"Customer ID: {customer_id}")
print(f"Customer Name: {customer_name}")
print(f"City: {city}")
print(f"Balance: ${balance}")

"""customers = ["C001", "C002", "C003" , "C004"]
print(customers)
print(customers[0])
for cust in customers:
    print(cust)"""

'''

customer = {"customer_id":"C001", "name":"Amit", "city" : "Pune"}
print(customer)
print{customer["name"]}
for k,v in customer.items():
    print(f'{k}={v}')
    '''

def classify_transaction(amount):
    if amount < 1000:
        return "low"
    elif amount < 10000:
        return "medium"
    else:
        return "high"

print(classify_transaction
      (850));
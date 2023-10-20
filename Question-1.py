# Inventory Management
inventory = {}

def add_item(name, quantity, price):
    inventory[name] = {'quantity': quantity, 'price': price}

def update_item(name, new_quantity, new_price):
    if name in inventory:
        inventory[name]['quantity'] = new_quantity
        inventory[name]['price'] = new_price

def remove_item(name):
    if name in inventory:
        del inventory[name]

def generate_inventory_report():
    print("Inventory Report:")
    for item, details in inventory.items():
        print(f"{item} - Quantity: {details['quantity']}, Price: ${details['price']}")

# Sales and Customer Database
sales_data = []

def record_sale(customer_name, items_purchased):
    total_price = sum(inventory[item]['price'] * quantity for item, quantity in items_purchased.items())
    sales_data.append({'customer_name': customer_name, 'items_purchased': items_purchased, 'total_price': total_price})

def calculate_total_sales():
    total_sales = sum(sale['total_price'] for sale in sales_data)
    return total_sales

# Example usage
add_item("Item1", 10, 5.99)
add_item("Item2", 20, 10.99)

record_sale("Customer1", {"Item1": 1, "Item2": 0})
record_sale("Customer2", {"Item1": 0})

generate_inventory_report()
print("\nTotal Sales:", calculate_total_sales())

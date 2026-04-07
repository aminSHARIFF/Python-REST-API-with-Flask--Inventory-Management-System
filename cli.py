import requests

BASE_URL = "http://127.0.0.1:5000"

def show_menu():
    print("\n===== Sharif Inventory System =====")
    print("1. View all inventory")
    print("2. View single item")
    print("3. Add new item")
    print("4. Update item")
    print("5. Delete item")
    print("6. Lookup product by barcode")
    print("7. Exit")

def view_all():
    response = requests.get(f"{BASE_URL}/inventory")
    items = response.json()
    for item in items:
        print(f"\nID: {item['id']} | Name: {item['name']} | Brand: {item['brand']} | Price: ${item['price']} | Qty: {item['quantity']}")

def view_one():
    id = input("Enter item ID: ")
    response = requests.get(f"{BASE_URL}/inventory/{id}")
    print(response.json())

def add_item():
    name = input("Name: ")
    brand = input("Brand: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    barcode = input("Barcode: ")
    data = {"name": name, "brand": brand, "price": price, "quantity": quantity, "barcode": barcode}
    response = requests.post(f"{BASE_URL}/inventory", json=data)
    print("Added:", response.json())

def update_item():
    id = input("Enter item ID to update: ")
    price = float(input("New price: "))
    quantity = int(input("New quantity: "))
    data = {"price": price, "quantity": quantity}
    response = requests.patch(f"{BASE_URL}/inventory/{id}", json=data)
    print("Updated:", response.json())

def delete_item():
    id = input("Enter item ID to delete: ")
    response = requests.delete(f"{BASE_URL}/inventory/{id}")
    print(response.json())

def lookup_barcode():
    barcode = input("Enter barcode: ")
    response = requests.get(f"{BASE_URL}/lookup/{barcode}")
    data = response.json()
    if 'error' in data:
        print("Product not found")
    else:
        print(f"Name: {data['name']} | Brand: {data['brand']}")
        add = input("Add to inventory? (yes/no): ")
        if add == "yes":
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
            new_item = {"name": data['name'], "brand": data['brand'], "price": price, "quantity": quantity, "barcode": barcode}
            requests.post(f"{BASE_URL}/inventory", json=new_item)
            print("Added to inventory!")

while True:
    show_menu()
    choice = input("\nEnter choice (1-7): ")
    if choice == "1":
        view_all()
    elif choice == "2":
        view_one()
    elif choice == "3":
        add_item()
    elif choice == "4":
        update_item()
    elif choice == "5":
        delete_item()
    elif choice == "6":
        lookup_barcode()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again")
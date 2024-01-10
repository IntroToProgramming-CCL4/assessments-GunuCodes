import random

#This function facilitates the addition of items to the user's basket, checking for stock availability
#and relaying that information back to the user's screen.

def add_to_basket(items_in_stock, basket, item_choice, quantity):
    item = items_in_stock[item_choice]
    if item['stock'] >= quantity:
        for _ in range(quantity):
            basket.append(item)
            item['stock'] -= 1
        print(f"{quantity} {item['item_name']}(s) added to your basket.")
        smart_suggestion(items_in_stock, basket)
    else:
        print(f"Sorry, {item['item_name']} is out of stock or insufficient stock for the requested quantity.")

#This function give the user an overview of their selected items during the shopping process.
#It checks whether the basket is empty or not and returns the total price of all the items inside if there are.
        
def view_basket(basket):
    if basket:
        total_price = sum(item['item_price'] for item in basket)
        print("\nItems in your basket:")
        for item in basket:
            print(f"• {item['item_name']} - ${item['item_price']}")
        print(f"Total: ${total_price}")
        return total_price
    else:
        print("\nYour basket is empty.")
        return 0
    
#This function handles the checkout process of the Vending Machine.
#It is responsible for finalizing the user's purchase, calculating the user's funds and remaining balance, and dispensing items.

def checkout(basket, total_money):
    print("\nChecking out...")
    total_cost = view_basket(basket)
    remaining_balance = total_money
    while total_cost > 0:
        if remaining_balance >= total_cost:
            remaining_balance -= total_cost
            basket = []  
            print(f"Your change is: ${remaining_balance}")
            print("\nYour items have been dispensed.")
            print("\n------- Thank you for using the Express Medicine Vending Machine! -------")
            break
        else:
            print("Insufficient funds. Please add more money.")
            additional_money = int(input("Please input additional money: "))
            remaining_balance += additional_money
    if total_cost == 0:
        print("\nNo items in the basket. Nothing to checkout.")
        print("\n------- Thank you for using the Express Medicine Vending Machine! -------")

#This function provides a recommendation to the user for an additional item based on the last item that wasadded to their basket.
#It's not actually smart, it just recommends a different random item from the same category of the initial item that the user bought.
        
def smart_suggestion(items_in_stock, basket):
    if basket:
        item = items_in_stock
        
        last_purchase = basket[-1]["item_name"]
        category = basket[-1]["category"]
        available_items = [item for item in items_in_stock if item["category"] == category and item["item_name"] != last_purchase]
        if available_items:
            suggested_item = random.choice(available_items)
            print("\nOther customers like you also purchased:")
            print(f"{suggested_item['item_name']} - ${suggested_item['item_price']} - Item ID: {suggested_item['item_id']} ")

#This section essentially sets up the initial inventory for the Express Medicine Vending Machine. 
#Users can input item codes to make purchasess. The program checks for item availability and updates the user's basket accordingly. 

def run():
    print("\n------- Welcome to the Express Medicine Vending Machine! -------\n\n")
    categories = {"General Health Products": [], "Antibiotics": [], "Skin Care": []}
    
    items_in_stock = [
        {"item_id": 1, "item_name": "Bandage", "item_price": 2, "stock": 20, "category": "General Health Products"},
        {"item_id": 2, "item_name": "Antiseptic Cream", "item_price": 20, "stock": 3, "category": "General Health Products"},
        {"item_id": 3, "item_name": "Eye Drops", "item_price": 5, "stock": 7, "category": "General Health Products"},
        {"item_id": 4, "item_name": "Cough Syrup", "item_price": 15, "stock": 4, "category": "General Health Products"},
        {"item_id": 5, "item_name": "Throat Lozenges", "item_price": 5, "stock": 8, "category": "General Health Products"},
        {"item_id": 6, "item_name": "Hand Sanitizer", "item_price": 6, "stock": 8, "category": "General Health Products"},
        {"item_id": 7, "item_name": "Paracetamol", "item_price": 10, "stock": 10, "category": "General Health Products"},
        {"item_id": 8, "item_name": "Ozempic", "item_price": 50, "stock": 2, "category": "Antibiotics"},
        {"item_id": 9, "item_name": "Aspirin", "item_price": 40, "stock": 6, "category": "Antibiotics"},
        {"item_id": 10, "item_name": "Ibuprofen", "item_price": 10, "stock": 10, "category": "Antibiotics"},
        {"item_id": 11, "item_name": "Hydrogen Peroxide", "item_price": 12, "stock": 12, "category": "Antibiotics"},
        {"item_id": 12, "item_name": "Sunscreen", "item_price": 15, "stock": 2, "category": "Skin Care"},
        {"item_id": 13, "item_name": "Moisturizing Cream", "item_price": 20, "stock": 6, "category": "Skin Care"},
        {"item_id": 14, "item_name": "Lip Balm", "item_price": 4, "stock": 9, "category": "Skin Care"},
        {"item_id": 15, "item_name": "Acne Treatment Gel", "item_price": 15, "stock": 2, "category": "Skin Care"},
    ]

    basket = []

    for i in items_in_stock:
        categories[i['category']].append(
            (f"Item ID: {i['item_id']} --- Price: ${i['item_price']} --- Item: {i['item_name']} --- Stock: {i['stock']}")
        )

    category_order = ["General Health Products", "Antibiotics", "Skin Care"]

    for category in category_order:
        print(f"\n{category}:\n")
        for item in categories[category]:
            print(item)

    run = True
    while run:
        view_basket(basket)  
        buy_item = int(input("\nEnter the item code of the product you want to buy (or type '0' to checkout): "))
        if buy_item == 0:
            break
        elif 1 <= buy_item <= len(items_in_stock):
            quantity = int(input(f"How many {items_in_stock[buy_item - 1]['item_name']}(s) would you like to buy? "))
            if quantity > 0:
                if items_in_stock[buy_item - 1]['stock'] >= quantity:
                    add_to_basket(items_in_stock, basket, buy_item - 1, quantity)
                else:
                    print("\nSorry! There is no more stock left for the requested quantity.")
            else:
                print("\nInvalid quantity entered!")
        else:
            print("\nInvalid product ID!")
    
    total_money = int(input("\nPlease input the amount of money here: "))
    checkout(basket, total_money)

run()

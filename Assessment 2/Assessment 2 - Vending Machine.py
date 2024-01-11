import random

#This function facilitates the addition of items to the user's basket.
#It also handles stock availability.

def add_to_basket(items_in_stock, basket, item_choice, quantity):
    #Check if the requested quantity of the item is available in stock.
    item = items_in_stock[item_choice]
    if item['stock'] >= quantity:
        #Adds the item to the basket and update the stock amount.
        for _ in range(quantity):
            basket.append(item)
            item['stock'] -= 1
        print(f"{quantity} {item['item_name']}(s) added to your basket.")
        #Suggests other items the user might be interested in.
        smart_suggestion(items_in_stock, basket)
    else:
        #Informs the user if the item is out of stock or not enough quantity is available.
        print(f"Sorry, {item['item_name']} is out of stock or insufficient stock for the requested quantity.")

#This function is responsible for the removal of items from the user's basket.        

def remove_from_basket(basket):
    #Check if the basket is empty before attempting to remove an item.
    if not basket:
        return

    #Display the items in the basket for the user to choose which to remove.
    print("\nItems in your basket:")
    for i, item in enumerate(basket, start=1):
        print(f"{i}. {item['item_name']} - ${item['item_price']}")

    #Get the user's input for the item to remove.
    item_to_remove = int(input("\nEnter the number of the item you want to remove (or type '0' to cancel): "))
    if item_to_remove == 0:
        return
    elif 1 <= item_to_remove <= len(basket):
        #Remove the selected item from the basket and update the stock amount accordingly.
        item = basket.pop(item_to_remove - 1)
        print(f"\n{item['item_name']} has been removed from your basket.")
        item['stock'] += 1
    else:
        #Handle invalid input for item removal.
        print("\nInvalid number. Please enter a valid number.")

#This function give the user an overview of their items in their basket.
#It checks whether the basket is empty or not and returns the total price of all the items inside if there are.
        
def view_basket(basket):
    #Calculate and display the total price of items in the basket.
    if basket:
        total_price = sum(item['item_price'] for item in basket)
        print("\nItems in your basket:")
        for item in basket:
            print(f"• {item['item_name']} - ${item['item_price']}")
        print(f"Total: ${total_price}")
        return total_price
    else:
        #Informs the user if the basket is empty.
        print("\nYour basket is empty.")
        return 0

def checkout(basket, total_money):
    #Begins the checkout process and display the basket contents.
    print("\nChecking out...")
    total_cost = view_basket(basket)
    remaining_balance = total_money
    while total_cost > 0:
        #Check if the user has enough money to pay for the items.
        if remaining_balance >= total_cost:
            #Complete the transaction and clear the basket.
            remaining_balance -= total_cost
            basket.clear()
            print(f"Your change is: ${remaining_balance}")
            print("\nYour items have been dispensed.")
            print("\n------- Thank you for using the Express Medicine Vending Machine! -------")
            break
        else:
            #Prompt the user to add more money in case of insufficient funds.
            print("Insufficient funds. Please add more money.")
            additional_money = int(input("Please input additional money: "))
            remaining_balance += additional_money
    #Handle the case where there are no items to checkout.
    if total_cost == 0:
        print("\nNo items in the basket. Nothing to checkout.")
        print("\n------- Thank you for using the Express Medicine Vending Machine! -------")

#This function provides a recommendation to the user for an additional item based on the last item that wasadded to their basket.
#It's not actually smart, it just recommends a different random item from the same category of the last purchased item that the user bought, excluding that item itself.
        
def smart_suggestion(items_in_stock, basket):
    #Suggests an item to the user based on the last item added to the basket.
    if basket:
        last_purchase = basket[-1]["item_name"]
        category = basket[-1]["category"]
        # Filter available items in the same category but not the same as the last purchase.
        available_items = [item for item in items_in_stock if item["category"] == category and item["item_name"] != last_purchase]
        if available_items:
            # Randomly selects an item to suggest.
            suggested_item = random.choice(available_items)
            print("\nOther customers like you also purchased:")
            print(f"{suggested_item['item_name']} - ${suggested_item['item_price']} - Item ID: {suggested_item['item_id']} ")

#The main part of the program. This entire section simulates the entire logical processes of a typical Vending Machine.
#The intiial inventory of the vending machine is also initialized here, with all their corresponding attributes such as their names and prices.
            
def run():
    #Initialize the inventory and display available items to the user.
    print("\n------- Welcome to the Express Medicine Vending Machine! -------\n")
    categories = {
        "General Health Products": [],
        "Antibiotics": [],
        "Skin Care": []
    }
    #Add items to each category.
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
    #Display each category and its items.
    for item in items_in_stock:
        categories[item['category']].append(item)
    for category, items in categories.items():
        print(f"\n{category}:")
        for item in items:
            print(f"Item ID: {item['item_id']} --- Price: ${item['item_price']} --- Item: {item['item_name']} --- Stock: {item['stock']}")

    #Main user-interaction loop.
    while True:
        #Shows the basket and prompt the user for the next action.
        view_basket(basket)
        action = input("\nEnter 'b' to buy an item, 'r' to remove an item, or 'c' to checkout: ")
        if action.lower() == 'b':
            #Handle purchases of items.
            buy_item = int(input("\nEnter the item code of the product you want to buy: "))
            item_to_buy = next((item for item in items_in_stock if item['item_id'] == buy_item), None)
            if item_to_buy:
                quantity = int(input(f"How many {item_to_buy['item_name']}(s) would you like to buy? "))
                if quantity > 0:
                    if item_to_buy['stock'] >= quantity:
                        add_to_basket(items_in_stock, basket, items_in_stock.index(item_to_buy), quantity)
                    else:
                        print("\nSorry! There is no more stock left for the requested quantity.")
                else:
                    print("\nInvalid quantity. Please enter a positive number.")
            else:
                print("\nInvalid item code. Please enter a valid item code.")
        elif action.lower() == 'r':
            #Handle  removal of items from the basket.
            remove_from_basket(basket)
        elif action.lower() == 'c':
            #Ends loop and moves to checkout.
            break
        else:
            #Handle case of invalid input.
            print("\nInvalid input. Please enter 'b', 'r', or 'c'.")

    #Checkout if there are items in the basket, otherwise end the program.
    if basket:
        total_money = int(input("\nPlease input your total money: "))
        checkout(basket, total_money)
    else:
        print("\nNo items in the basket. Nothing to checkout.")
        print("\n------- Thank you for using the Express Medicine Vending Machine! -------")

#Starts the vending machine program.
run()

#all values in CAD per ticket
items = {
        "OpenAI Credits": 3.425,
        "Domain": 3.425,
        "Notebook": 3.288,
        "Logic Analyzer": 3.4,
        "Breadboard": 2.5,
        "Multimeter": 2.14,
        "Arcade Ticket Counter": 2.14,
        "Soldering Iron": 3.75,
        "Pinecil": 3,
        "Yubikey": 5.022,
        "Keycaps": 1.826,
        "Octocat": 1.933,
        "Wacom": 3.2,
        "Backpack": 3.67,
        "Flipper": 3.32,
        "Keyboard": 3.1,
        "Framework Factory Seconds": 5.66,
        "Prusa": 4.51,
        "Bambu Lab": 3.33,
        "Framework 13 Inch": 10.9,
        "Quest 3": 3.25,
        "Framework 16 Inch": 5.75,
        "Macbook": 3.8725
    }

# #returns value in CAD per ticket 
# def calculate_price_per_ticket(item_name):
#         tickets, price = items[item_name]
#         return price / tickets

# print("Press 1 to find the price per ticket for an item.")
# #print("Press 2 to find the most valuable items for a given number of tickets.")
# choice = int(input("Enter your choice: "))

# if choice == 1:
#     item_name = input("Enter the name of the item: ")
#     if item_name in items:
#         price_per_ticket = calculate_price_per_ticket(item_name)
#         print("the value of a " + item_name + " is " + str(price_per_ticket))
#     else:
#         print("item not found, check for typos and try again")

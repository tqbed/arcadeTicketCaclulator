#all values in CAD 
items = {
        "OpenAI Credits": [4, 13.7],
        "Domain": [4, 13.7],
        "Notebook": [5, 16.44],
        "Logic Analyzer": [5, 17],
        "Breadboard": [6, 15],
        "Multimeter": [7, 15],
        "Arcade Ticket Counter": [7, 15],
        "Soldering Iron": [8, 30],
        "Pinecil": [14, 42],
        "Yubikey": [15, 75.33],
        "Keycaps": [15, 27.39],
        "Octocat": [15, 29],
        "Wacom": [25, 80],
        "Backpack": [50, 183.53],
        "Flipper": [70, 232.85],
        "Keyboard": [75, 232.85],
        "Framework Factory Seconds": [120, 679],
        "Prusa": [130, 587],
        "Bambu Lab": [135, 450],
        "Framework 13 Inch": [175, 1909],
        "Quest 3": [200, 650],
        "Framework 16 Inch": [400, 2299],
        "Macbook": [400, 1549]
    }

#sorts everything into an ordered array of most value to least
#then figures out how many items you can buy with the tickets you have going down the list 
def find_valuable_items():
    global user_tickets
    global past_user_tickets
    
    valuable_items = {item: (price[1] / price[0]) for item, price in items.items()}
    sorted_valuable_items = sorted(valuable_items.items(), key=lambda x: x[1], reverse=True)

    print("Based on your " + str(user_tickets) + " tickets, the most valuable items you can get are:")
    for item, value in sorted_valuable_items:
        if user_tickets - items[item][0] >= 0:
            user_tickets -= items[item][0]
            past_user_tickets = user_tickets
            print(item + ": " + str(value) + " CAD per ticket (" + str(user_tickets) + " tickets remaining)")
        else:
            user_tickets = past_user_tickets

#prompt user, program start!
print("Press 1 to find the price per ticket for an item.")
print("Press 2 to find the most valuable items for a given number of tickets.")
choice = int(input("Enter your choice: "))

#just find values for a single item 
if choice == 1:
    item_name = input("Enter the name of the item: ")
    if item_name in items:
        price_per_ticket = items[item_name][1] / items[item_name][0]
        print("the value of a " + item_name + " is " + str(price_per_ticket) + " CAD per ticket")
    else:
        print("item not found, check for typos and try again")

#finds as many purchasable valuable items for given ticket number           
elif choice == 2:
    user_tickets = int(input("Enter the number of tickets you have: "))
    past_user_tickets = user_tickets
        
    if user_tickets <= 0:
        print("You must enter a positive number of tickets")
    else:
        find_valuable_items()    
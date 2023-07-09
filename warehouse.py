

balance = 0
price = 0
inventory_storage = {
    "pen": {"price_per_unit": "1", "quantity": 30},
    "book": {"price_per_unit":"15", "quantity": 15}, 
    "bag": {"price_per_unit":"30", "quantity": 20},
    "copier": {"price_per_unit":"200", "quantity": 5}
}
history = []
product_list = ['pen', 'book', 'bag', 'copier']
amount = 0
total_amount = 0
quantity = 0

commands = ['balance', 'sale', 'purchase', 'account', 'list', 'warehouse', 'review', 'end']

print("Welcome to our warehouse!")
print("Here are the options: 'balance', 'sale', 'purchase', 'account', 'list', 'warehouse', 'review', 'end'")

while True:
    command = input ("Please enter a command: ")

    if command == "balance":
        amount = float(input("Enter amount:"))
        action = input("Enter add or subtract to you balance: ")
        if action == 'add':
            balance += amount
            print("Balance added.")
        if action == 'subtract':
            if balance - amount < 0:
                print("Insufficient balance!")
            elif balance - amount > 0:
                balance = balance - amount
        
        history.append(action)
        history.append(amount)             
          
    
    elif command == "sale":
        item = input("Enter product name: ")
        quantity = int(input("Enter quantity:"))
        price = float(input("Enter product price: "))

        total_price = price * quantity
        balance += total_price
        print(f"Balance: {total_price}")

        if item not in inventory_storage:
            print("Item not found.")
           
        if item in inventory_storage > quantity:
            total_price = price * quantity
            balance += total_price
            print(f"Balance: {total_price}")
                
        if item in inventory_storage < quantity:
            print("Insufficient quantity in warehouse.")
            

        history.append(quantity)
        history.append(item)
        history.append(price)
        history.append(balance)

    elif command == "purchase":
        item = input ("Enter product name:")
        quantity = int(input("Enter quantity:"))
        price = float(input("How much does it cost?: "))

        total_price = quantity * price
        if balance - price * quantity < 0:
            print("Insufficient balance.")
        

    elif command == "account":
        account = balance - price * quantity
        history.append(price)
        history.append(product_list)
        history.append(quantity)
        print(f"Display account balance: {account}")

        
    elif command == "list":
        for product in product_list:
            print([product_list])
        

    elif command == "warehouse":
        find_product = input ("Enter product name:")
        product_status = inventory_storage.get(find_product)
        if find_product in inventory_storage:
            print("Item found.")
        else:
            print("Item not found.")    


    elif command == "review": 
        log = input("Enter 'History' to display full history, otherwise enter 'range' for specific info:")

        if log == 'History':
            print(f"History: ")
            

        elif log == 'range':
            range = input("Enter 'from' and 'to' to display specific values: ")
            range = len(log)
            history_from = int(input("From: "))
            history_to =int(input("To:"))
            if log < history_to:
                print("incorrect value.")
            else:
                print(history[history_from: history_to])    


    elif command == "end":
        print("Ending program.")
        break




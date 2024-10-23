from shop import Shop

aspireShop = Shop("AlgoAspireShop")
curr_user = None
is_seller = False

while True:
    if curr_user == None:
        print(f"\n--------Welcome to {aspireShop.name}---------")
        print("1. Customer Registration")
        print("2. Customer Login")
        print("3. Seller Registration")
        print("4. Seller Login")
        print("5. Exit")

        op = input(">>> ")
        if op == "1":
            name = input("Enter your name: ")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            curr_user = aspireShop.customer_register(name, username, password)

            if curr_user != None:
                is_seller = False

        elif op == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            curr_user = aspireShop.customer_login(username, password)

            if curr_user != None:
                is_seller = False

        if op == "3":
            name = input("Enter your name: ")
            address = input("Enter your address: ")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            curr_user = aspireShop.seller_register(name, address, username, password)

            if curr_user != None:
                is_seller = True

        elif op == "4":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            curr_user = aspireShop.seller_login(username, password)

            if curr_user != None:
                is_seller = True
        
        elif op == "5":
            exit()

    else:
        if is_seller:
            print("\n------Seller Menu-------")
            print(f"@{curr_user.username}")
            print("1. Add product")
            print("2. Remove Product")
            print("3. My products")
            print("4. Logout")
            
            op = input(">>> ")
            if op == "1":
                prod_name = input("Enter product name: ")
                prod_price = int(input("Enter product price: "))
                prod_quan = int(input("Enter product quantity: "))
                curr_user.add_product(aspireShop, prod_name, prod_price, prod_quan)

            elif op == "2":
                prod_name = input("Enter product name: ")
                curr_user.remove_product(aspireShop, prod_name)
            
            elif op == "3":
                curr_user.show_my_products(aspireShop)
            
            elif op == "4":
                print(f"@{curr_user.username} Logged out!")
                curr_user = None
            
            else:
                print("Invalid input!")

        else:
            print("\n-------Customer Menu-------")
            print(f"@{curr_user.username}")
            print("1. Show All Products")
            print("2. Add to Cart")
            print("3. Remove from Cart")
            print("4. My Cart")
            print("5. Place Order")
            print("6. Logout")

            op = input(">>> ")
            if op == "1":
                curr_user.show_all_products(aspireShop)
            
            elif op == "2":
                prod_name = input("Enter product name: ")
                prod_quan = int(input("Enter product quantity: "))
                curr_user.add_to_cart(aspireShop, prod_name, prod_quan)

            elif op == "3":
                prod_name = input("Enter product name: ")
                curr_user.remove_from_cart(aspireShop, prod_name)
            
            elif op == "4":
                curr_user.my_cart()

            elif op == "5":
                amount = int(input("Enter amount: $"))
                curr_user.place_order(amount)

            elif op == "6":
                print(f"@{curr_user.username} Logged out!")
                curr_user = None
            
            else:
                print("Invalid input!")

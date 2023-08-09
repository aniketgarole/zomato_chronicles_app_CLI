def mainFun():
    while True:
        try:

            choice = int(input("""\n\n           ********** Welcome to Mumbai Munchies **********
                
                Please choose from the options below
                1. Add snack to inventory
                2. Remove snack from inventory
                3. Change availabililty of snack (yes/no)
                4. Order snack
                5. View inventory
                6. View orders
                7. Change order status              
                8. Exit
                
                """))
            

            if choice == 8:
                print("\n           Thank you for the visit. Have a good day 😊")
                print("\n           ********************************************\n")
                break
            
            
            elif choice == 1:
                id = (input("            Enter snack id (number): "))
                name = input("            Enter snack name: ")

                while True:

                    try:
                        price = int(input("            Enter snack price: "))
                        break
                    except ValueError: 
                        print("\n            Please enter a number for price\n")
                        continue

                while True:
                    avail = input("            Enter snack availability (yes/no): ").lower()
                    if avail != "yes" and avail != "no":
                        print("\n            Please enter either 'yes' or 'no', no other values are accepted")
                    else:
                        break

                while True:

                    try:
                        quantity = int(input("            Enter snack quantity: "))
                        break
                    except ValueError: 
                        print("\n            Please enter a number for quantity\n")
                        continue


                snack = {
                    "id": id, 
                    "name": name, 
                    "price": price, 
                    "avail": avail,
                    "quantity": quantity
                    }
                
           
           
        except ValueError:
                
                print("\n            Invalid option, choose the valid option!!")  

                


            



mainFun()
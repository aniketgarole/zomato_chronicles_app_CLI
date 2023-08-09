import uuid


def addSnack(snack):
    with open("../data/snacks.txt", "r") as file:
        contents = file.read()
        if contents == "":
            list = []
        else:
            list = eval(contents)
        
        list.append(snack)
        
        with open("../data/snacks.txt", "w") as filew:
            filew.write(str(list))
            print("\n            Snack has been added to the inventory successfully!!\n")
           





def mainFun():
    while True:
        try:

            choice = int(input("""\n\n           ********** Welcome to Mumbai Munchies **********
                
                Please choose from the options below
                1. Add dish to inventory
                2. Remove dish from inventory
                3. Change availabililty of dish (yes/no)
                4. Order dish
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
                id = (input("            Enter dish id (number): "))
                name = input("            Enter dish name: ")

                while True:

                    try:
                        price = int(input("            Enter dish price: "))
                        break
                    except ValueError: 
                        print("\n            Please enter a number for price\n")
                        continue

                while True:
                    avail = input("            Enter dish availability (yes/no): ").lower()
                    if avail != "yes" and avail != "no":
                        print("\n            Please enter either 'yes' or 'no', no other values are accepted")
                    else:
                        break

                while True:

                    try:
                        quantity = int(input("            Enter dish quantity: "))
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
                
                addSnack(snack)
           
        except ValueError:
                
                print("\n            Invalid option, choose the valid option!!")  

                


            



mainFun()
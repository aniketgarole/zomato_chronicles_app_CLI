import uuid


def addDish(snack):
    with open("../data/dishes.txt", "r") as file:
        contents = file.read()
        if contents == "":
            list = []
        else:
            list = eval(contents)
        
        list.append(snack)
        
        with open("../data/dishes.txt", "w") as filew:
            filew.write(str(list))
            print("\n            Snack has been added to the inventory successfully!!\n")
           


def removeDish(id):
    with open("../data/dishes.txt", "r") as filer:
        contents = filer.read() 
        if contents == "":
            list = []
            print("\n            Sorry, the inventory is empty")
            return False

        else:
            list = eval(contents)
            
            deleted_snack = [x for x in list if x["id"] == id]
            
            if (len(deleted_snack)):
                new_list = [x for x in list if x["id"] != id]

                with open("../data/dishes.txt", "w") as filew:
                    filew.write(str(new_list))
                    print("\n            Snack has been removed successfully!!\n")
                    return True

            else:
                print(f"\n            The snack with id {id} does not exist, please try different id")
                return False





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


                dish = {
                    "id": id, 
                    "name": name, 
                    "price": price, 
                    "avail": avail,
                    "quantity": quantity
                    }
                
                addDish(dish)

            
            elif choice == 2:
                flag = False
                while True:
                    remove_id = input("\n            Enter id to remove snack or enter 'back' to go back to menu: ")

                    if remove_id != "back":

                        value = removeDish(remove_id)

                        if value:
                            break
                        else:
                            flag = True
                            break
                            
                    
                    else:
                        flag = True
                        break

                if flag:
                    continue
           
        except ValueError:
                
                print("\n            Invalid option, choose the valid option!!")  

                


            



mainFun()
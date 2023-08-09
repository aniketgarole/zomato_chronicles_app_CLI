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
            

           
           
        except ValueError:
                
                print("\n            Invalid option, choose the valid option!!")  

                


            



mainFun()
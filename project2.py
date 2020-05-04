#Idea; Create a shopping expereince and total purchase. Chipotle
def menu():

    #Intro
    print("\n Welcome to Chipotle! \n")
    print("What would you like to order? \n")
    check = 0
    price = 0.00
    #Vessel
    while check < 3:
        vessel = input("1. Burrito\n2. Bowl\n3. Taco\n")
        if (vessel == "1"):
            print("Good Choice!\n")
            vessel = "Burrito\n"
            check = 3
        elif (vessel == "2"):
            print("Good Choice!\n")
            vessel = "Bowl\n"
            check = 3
        elif (vessel == "3"):
            print("Good Choice!\n")
            vessel = "Taco\n"
            check = 3
        else:
            print("Sorry you have made an invalid selection. Please try again.\n")
            check += 1
            if check == 3:
                print("Good Bye.\n")
                exit()
    check = 0

    #Meat
    while check < 3:
        meat = input("what type of meat would you like? \n1. Chicken\n2. Steak\n3. Barbacoa\n4. Carnitas\n5. Sofritas\n6. Veggie\n")
        if (meat == "1"):
            print("Good Choice!\n")
            meat = "Chicken\n"
            price += 6.75
            check = 3
        elif (meat == "2"):
            print("Good Choice!\n")
            meat = "Steak\n"
            price += 7.25
            check = 3
        elif (meat == "3"):
            print("Good Choice!\n")
            meat = "Barbacoa\n"
            price += 8.45
            check = 3
        elif (meat == "4"):
            print("Good Choice!\n")
            meat = "Carnitas\n"
            price += 8.20
            check = 3
        elif (meat == "5"):
            print("Good Choice!\n")
            meat = "Sofritas\n"
            price += 7.90
            check = 3
        elif (meat == "6"):
            print("Good Choice!\n")
            meat = "Veggie\n"
            price += 6.50
            check = 3
        else:
            print("Sorry you have made an invalid selection. Please try again.\n")
            check += 1
            if check == 3:
                print("Good Bye.\n")
                exit()
    check = 0

    #Base
    while check < 3:
        base = input("1. White Rice\n2. Brown Rice\n3. Lettuce\n")
        if (base == "1"):
            print("Good Choice!\n")
            base = "White Rice\n"
            check = 3
        elif (base == "2"):
            print("Good Choice!\n")
            base = "Brown Rice\n"
            check = 3
        elif (base == "3"):
            print("Good Choice!\n")
            base = "Lettuce\n"
            check = 3
        else:
            print("Sorry you have made an invalid selection. Please try again.\n")
            check += 1
            if check == 3:
                print("Good Bye.\n")
                exit()
    check = 0

    #Beans
    while check < 3:
        beans = input("1. Black Beans\n2. Pinto Beans\n3. No Beans\n")
        if (beans == "1"):
            print("Good Choice!\n")
            beans = "Black Beans\n"
            check = 3
        elif (beans == "2"):
            print("Good Choice!\n")
            beans = "Pinto Beans\n"
            check = 3
        elif (beans == "3"):
            print("Good Choice!\n")
            beans = "No Beans\n"
            check = 3
        else:
            print("Sorry you have made an invalid selection. Please try again.\n")
            check += 1
            if check == 3:
                print("Good Bye.\n")
                exit()
    check = 0

    #Topings
    while check < 3:
        queso = input("Would you like Queso? It will cost extra. \n").lower()
        if(queso == "y" or queso == "yes"):
            queso = "Queso\n"
            price += 1.25
            print("Good Choice!\n")
            check = 3
        elif(queso == "n" or queso == "no"):
            queso = ""
            print("Good Choice!\n")
            check = 3
        else:
            print("Sorry you have made an invalid selection. Please try again.\n")
            check += 1
            if check == 3:
                print("Good Bye.\n")
                exit()
    check = 0

    while check < 3:
        guac = input("Would you like Guac? It will cost extra. \n").lower()
        if(guac == "y" or guac == "yes"):
            guac = "Guac\n"
            price += 2.15
            print("Good Choice!\n")
            check = 3
        elif(guac == "n" or guac == "no"):
            guac = ""
            print("Good Choice!\n")
            check = 3
        else:
            print("Sorry you have made an invalid selection. Please try again.\n")
            check += 1
            if check == 3:
                print("Good Bye.\n")
                exit()
    check = 0

    # Toppings
    while check < 3:
        fijita = input("Would you like Fijita? \n").lower()
        if(fijita == "y" or fijita == "yes"):
            fijita= input("How much Fijita would you like? \n1. Light\n2. Regular\n3. Extra\n")
            if(fijita == "1"):
                fijita = "Fijita: Light\n"
            elif(fijita == "2"):
                fijita = "Fijita: Regular\n"
            elif(fijita == "3"):
                fijita = "Fijita: Extra\n"
            else:
                print("Sorry you have made an invalid selection. Please try again.\n")
                exit()
            print("Good Choice!\n")
            check = 3
        elif(fijita == "n" or fijita == "no"):
            fijita = ""
            print("Good Choice!\n")
            check = 3
        else:
            print("Sorry you have made an invalid selection. Please try again.\n")
            check += 1
            if check == 3:
                print("Good Bye.\n")
                exit()
    check = 0

    while check < 3:
        corn = input("Would you like Corn? \n").lower()
        if(corn == "y" or corn == "yes"):
            corn = input("How much Corn would you like? \n1. Light\n2. Regular\n3. Extra\n")
            if(corn == "1"):
                corn = "Corn: Light\n"
            elif(corn == "2"):
                corn = "Corn: Regular\n"
            elif(corn == "3"):
                corn = "Corn: Extra\n"
            else:
                print("Sorry you have made an invalid selection. Please try again.\n")
                exit()
            print("Good Choice!\n")
            check = 3
        elif(corn == "n" or corn == "no"):
            corn = ""
            print("Good Choice!\n")
            check = 3
        else:
            print("Sorry you have made an invalid selection. Please try again.\n")
            check += 1
            if check == 3:
                print("Good Bye.\n")
                exit()
    check = 0

    while check < 3:
        salsa = input("Would you like Salsa? \n").lower()
        if(salsa == "y" or salsa == "yes"):
            salsa = input("How much Salsa would you like? \n1. Light\n2. Regular\n3. Extra\n")
            if(salsa == "1"):
                salsa = "Salsa: Light\n"
            elif(salsa == "2"):
                salsa = "Salsa: Regular\n"
            elif(salsa == "3"):
                Salsa = "Salsa: Extra\n"
            else:
                print("Sorry you have made an invalid selection. Please try again.\n")
                exit()
            print("Good Choice!\n")
            check = 3
        elif(salsa == "n" or salsa == "no"):
            corn = ""
            print("Good Choice!\n")
            check = 3
        else:
            print("Sorry you have made an invalid selection. Please try again.\n")
            check += 1
            if check == 3:
                print("Good Bye.\n")
                exit()
    check = 0

    while check < 3:
        sourCream = input("Would you like Sour Cream? \n").lower()
        if(sourCream == "y" or sourCream == "yes"):
            sourCream = input("How much Sour Cream would you like? \n1. Light\n2. Regular\n3. Extra\n")
            if(sourCream == "1"):
                sourCream = "Sour Cream: Light\n"
            elif(sourCream == "2"):
                sourCream = "Sour cream: Regular\n"
            elif(sourCream == "3"):
                sourCream = "Sour cream: Extra\n"
            else:
                print("Sorry you have made an invalid selection. Please try again.\n")
                exit()
            print("Good Choice!\n")
            check = 3
        elif(sourCream == "n" or sourCream == "no"):
            sourCream = ""
            print("Good Choice!\n")
            check = 3
        else:
            print("Sorry you have made an invalid selection. Please try again.\n")
            check += 1
            if check == 3:
                print("Good Bye.\n")
                exit()
    check = 0

    while check < 3:
        cheese = input("Would you like Cheese? \n").lower()
        if(cheese == "y" or cheese == "yes"):
            cheese = input("How much Cheese would you like? \n1. Light\n2. Regular\n3. Extra\n")
            if(cheese == "1"):
                cheese = "Cheese: Light\n"
            elif(cheese == "2"):
                cheese = "Cheese: Regular\n"
            elif(cheese == "3"):
                cheese = "Cheese: Extra\n"
            else:
                print("Sorry you have made an invalid selection. Please try again.\n")
                exit()
            print("Good Choice!\n")
            check = 3
        elif(cheese == "n" or cheese == "no"):
            cheese = ""
            print("Good Choice!\n")
            check = 3
        else:
            print("Sorry you have made an invalid selection. Please try again.\n")
            check += 1
            if check == 3:
                print("Good Bye.\n")
                exit()
    check = 0

    while check < 3:
        chips = input("Would you like Chips? It will cost extra. \n").lower()
        if(chips == "y" or chips == "yes"):
            chips = "Chips\n"
            price += 2.85
            print("Good Choice!\n")
            check = 3
        elif(chips == "n" or chips == "no"):
            chips = ""
            print("Good Choice!\n")
            check = 3
        else:
            print("Sorry you have made an invalid selection. Please try again.\n")
            check += 1
            if check == 3:
                print("Good Bye.\n")
                exit()
    check = 0

    while check < 3:
        drink = input("Would you like a Drink? It will cost extra. \n").lower()
        if(drink == "y" or drink == "yes"):
            drink = "Drink\n"
            price += 1.60
            print("Good Choice!\n")
            check = 3
        elif(drink == "n" or drink == "no"):
            drink = ""
            print("Good Choice!\n")
            check = 3
        else:
            print("Sorry you have made an invalid selection. Please try again.\n")
            check += 1
            if check == 3:
                print("Good Bye.\n")
                exit()
    check = 0

    #Combo discount
    if(chips == "Chips/n" and drink == "Drink\n"):
        price -= 1.00

    #Order Confirmation
    output = "Thank you for your purchase!\nBelow is your recipt:\n"
    output += vessel + base + meat + beans + queso + guac + fijita + corn + salsa + sourCream + cheese + chips + drink
    output +="******************************\n"
    output += "Total Price $" + str(price)
        #Recipt
    print(output)
menu()

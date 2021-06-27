MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

latte = MENU['latte']
latte_ing = latte['ingredients']
latte_water = latte_ing['water']
latte_coffee = latte_ing['coffee']
latte_milk = latte_ing['milk']
latte_cost = latte['cost']

espresso = MENU['espresso']
espresso_ing = espresso['ingredients']
espresso_water = espresso_ing['water']
espresso_coffee = espresso_ing['coffee']
espresso_cost = espresso['cost']

cappuccino = MENU['cappuccino']
cappuccino_ing = cappuccino['ingredients']
cappuccino_water = cappuccino_ing['water']
cappuccino_coffee = cappuccino_ing['coffee']
cappuccino_milk = cappuccino_ing['milk']
cappuccino_cost = cappuccino['cost']

trxn_status = 0

while True:
    print("What would you like? (espresso/latte/cappuccino):")
    drink = input()
    trxn_status = 0
    
    if drink == "no":
        print("No")

    elif drink == "espresso":
        if espresso_water < resources['water'] and espresso_coffee < resources['coffee'] and trxn_status == 0:

            print("Insert your coins")

            penny = int(input('Enter the number of Pennies: '))
            nickel = int(input('Enter the number of Nickels: '))
            dime = int(input('Enter the number of Dimes: '))
            quarter = int(input('Enter the number of Quarters: '))

            total_coins = 0.01 * penny + 0.05 * nickel + 0.10 * dime + 0.25 * quarter

            if total_coins == espresso_cost:
                money += total_coins
                resources['water'] = resources['water'] - espresso_water
                resources['coffee'] = resources['coffee'] - espresso_coffee
                print("Here is your Espresso. Enjoy!")
                trxn_status = 1
            if total_coins > espresso_cost:
                money += espresso_cost
                balance = total_coins - espresso_cost
                resources['water'] = resources['water'] - espresso_water
                resources['coffee'] = resources['coffee'] - espresso_coffee
                print("Here is $" + str(balance), "dollars in change.")
                print("Here is your Espresso. Enjoy!")
                trxn_status = 1
            if total_coins < espresso_cost:
                print("That's not enough money. Refunded $" + str(total_coins))
                trxn_status = 0
        if espresso_water == int(resources['water']) and espresso_coffee == int(resources['coffee'] and trxn_status == 0):
            print("Insert your coins")

            penny = int(input('Enter the number of Pennies: '))
            nickel = int(input('Enter the number of Nickels: '))
            dime = int(input('Enter the number of Dimes: '))
            quarter = int(input('Enter the number of Quarters: '))

            total_coins = 0.01 * penny + 0.05 * nickel + 0.10 * dime + 0.25 * quarter

            if total_coins == espresso_cost:
                money += total_coins
                resources['water'] = resources['water'] - espresso_water
                resources['coffee'] = resources['coffee'] - espresso_coffee
                print("Here is your Espresso. Enjoy!")
                trxn_status = 1

            if total_coins > espresso_cost:
                money += espresso_cost
                balance = total_coins - espresso_cost
                resources['water'] = resources['water'] - espresso_water
                resources['coffee'] = resources['coffee'] - espresso_coffee
                print("Here is $" + str(balance), "dollars in change.")
                print("Here is your Espresso. Enjoy!")
                trxn_status = 1

            if total_coins < espresso_cost:
                print("That's not enough money. Refunded $" + str(total_coins))
                trxn_status = 0

        elif resources['water'] < espresso_water or resources['coffee'] < espresso_coffee or trxn_status == 0:
            print("Not enough resources. Your inconvenience is regretted.")


    elif drink == "latte":
        if latte_water < int(resources['water']) and latte_coffee < int(resources['coffee']) and latte_milk < int(resources['milk']) and trxn_status == 0:

            print("Insert your coins")

            penny = int(input('Enter the number of Pennies: '))
            nickel = int(input('Enter the number of Nickels: '))
            dime = int(input('Enter the number of Dimes: '))
            quarter = int(input('Enter the number of Quarters: '))

            total_coins = 0.01 * penny + 0.05 * nickel + 0.10 * dime + 0.25 * quarter

            if total_coins == latte_cost:
                money += total_coins
                resources['water'] = resources['water'] - latte_water
                resources['coffee'] = resources['coffee'] - latte_coffee
                resources['milk'] = resources['milk'] - latte_milk
                print("Here is your latte. Enjoy!")
                trxn_status = 1

            if total_coins > latte_cost:
                money += latte_cost
                balance = total_coins - latte_cost
                resources['water'] = resources['water'] - latte_water
                resources['coffee'] = resources['coffee'] - latte_coffee
                resources['milk'] = resources['milk'] - latte_milk
                print("Here is $" + str(balance), "dollars in change.")
                print("Here is your latte. Enjoy!")
                trxn_status = 1

            if total_coins < latte_cost:
                print("That's not enough money. Refunded $" + str(total_coins))
                trxn_status = 0

        elif latte_water == int(resources['water']) and latte_coffee == int(resources['coffee']) and latte_milk == int(resources['milk']) and trxn_status == 0:
            print("Insert your coins")

            penny = int(input('Enter the number of Pennies: '))
            nickel = int(input('Enter the number of Nickels: '))
            dime = int(input('Enter the number of Dimes: '))
            quarter = int(input('Enter the number of Quarters: '))

            total_coins = 0.01 * penny + 0.05 * nickel + 0.10 * dime + 0.25 * quarter

            if total_coins == latte_cost:
                money += total_coins
                resources['water'] = resources['water'] - latte_water
                resources['coffee'] = resources['coffee'] - latte_coffee
                resources['milk'] = resources['milk'] - latte_milk
                print("Here is your latte. Enjoy!")
                trxn_status = 1

            if total_coins > latte_cost:
                money += latte_cost
                balance = total_coins - latte_cost
                resources['water'] = resources['water'] - latte_water
                resources['coffee'] = resources['coffee'] - latte_coffee
                resources['milk'] = resources['milk'] - latte_milk
                print("Here is $" + str(balance), "dollars in change.")
                print("Here is your latte. Enjoy!")
                trxn_status = 1

            if total_coins < latte_cost:
                print("That's not enough money. Refunded $" + str(total_coins))
                trxn_status = 0

        elif resources['water'] < latte_water or resources['coffee'] < latte_coffee or resources['milk'] < latte_milk or trxn_status == 0:
            print("Not enough resources. Your inconvenience is regretted.")

    elif drink == "cappuccino":
        if cappuccino_water < int(resources['water']) and cappuccino_coffee < int(resources['coffee']) and cappuccino_milk < int(resources['milk']) and trxn_status == 0:

            print("Insert your coins")

            penny = int(input('Enter the number of Pennies: '))
            nickel = int(input('Enter the number of Nickels: '))
            dime = int(input('Enter the number of Dimes: '))
            quarter = int(input('Enter the number of Quarters: '))

            total_coins = 0.01 * penny + 0.05 * nickel + 0.10 * dime + 0.25 * quarter

            if total_coins == cappuccino_cost:
                money += total_coins
                resources['water'] = resources['water'] - cappuccino_water
                resources['coffee'] = resources['coffee'] - cappuccino_coffee
                resources['milk'] = resources['milk'] - cappuccino_milk
                print("Here is your cappuccino. Enjoy!")
                trxn_status = 1

            if total_coins > cappuccino_cost:
                money += cappuccino_cost
                balance = total_coins - cappuccino_cost
                resources['water'] = resources['water'] - cappuccino_water
                resources['coffee'] = resources['coffee'] - cappuccino_coffee
                resources['milk'] = resources['milk'] - cappuccino_milk
                print("Here is $" + str(balance), "dollars in change.")
                print("Here is your cappuccino. Enjoy!")
                trxn_status = 1

            if total_coins < cappuccino_cost:
                print("That's not enough money. Refunded $" + str(total_coins))
                trxn_status = 0

        elif cappuccino_water == int(resources['water']) and cappuccino_coffee == int(resources['coffee']) and cappuccino_milk == int(resources['milk']) and trxn_status == 0:
            print("Insert your coins")

            penny = int(input('Enter the number of Pennies: '))
            nickel = int(input('Enter the number of Nickels: '))
            dime = int(input('Enter the number of Dimes: '))
            quarter = int(input('Enter the number of Quarters: '))

            total_coins = 0.01 * penny + 0.05 * nickel + 0.10 * dime + 0.25 * quarter

            if total_coins == cappuccino_cost:
                money += total_coins
                resources['water'] = resources['water'] - cappuccino_water
                resources['coffee'] = resources['coffee'] - cappuccino_coffee
                resources['milk'] = resources['milk'] - cappuccino_milk
                print("Here is your cappuccino. Enjoy!")
                trxn_status = 1

            if total_coins > cappuccino_cost:
                money += cappuccino_cost
                balance = total_coins - cappuccino_cost
                resources['water'] = resources['water'] - cappuccino_water
                resources['coffee'] = resources['coffee'] - cappuccino_coffee
                resources['milk'] = resources['milk'] - cappuccino_milk
                print("Here is $" + str(balance), "dollars in change.")
                print("Here is your cappuccino. Enjoy!")
                trxn_status = 1

            if total_coins < cappuccino_cost:
                print("That's not enough money. Refunded $" + str(total_coins))
                trxn_status = 0

        elif resources['water'] < cappuccino_water or resources['coffee'] < cappuccino_coffee or resources['milk'] < cappuccino_milk or trxn_status == 0:
            print("Not enough resources. Your inconvenience is regretted.")

    elif drink == "report":
        print("Water: " + str(resources['water']) + 'ml')
        print("Milk: " + str(resources['milk']) + 'ml')
        print("Coffee: " + str(resources['coffee']) + 'g')
        print("Money: $" + str(money))

    elif drink == "off":
        break

    else:
        print("you've entered an invalid option")

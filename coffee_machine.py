from utils.menu import MENU, resources
from utils.logo import logo
from time import sleep
from utils.helper import check_resources, cls, coin_processor, transaction


def turn_on():
    
    turn_off = False
    
    while not turn_off:
        print(f'{logo}\n')
        print('Welcome !\n')
        
        user_choice = input("What would you like? (espresso/latte/cappuccino) OR (press 'off' to leave)")

        if user_choice == 'off':
            turn_off = True
        
        elif user_choice == 'report':
            for data in resources:
                print(f'{data}: {resources[data]}')
            sleep(4)
            cls()
            turn_on()
       
        elif user_choice != 'espresso' and user_choice != 'latte' and user_choice != 'cappuccino':
            print('Invalid choice.')
            sleep(2)
            cls()
            turn_on()

        else:
            
            if check_resources(user_choice) != None:
                print(f'{check_resources(user_choice)}')
                sleep(3)
                cls()
                turn_on()
            
            else:    
                print(f'The price of your drink is ${MENU[user_choice]["cost"]:.2f}\n')
                print('Please insert the money: ')
                money = coin_processor(int(input('Quarters: ')), int(input('Dimes: ')), int(input('Nickles: ')), int(input('Pennies: ')))
                print(f'{transaction(money, user_choice)}\n')
                print(f'Enjoy your {user_choice}!')
                sleep(4)

                for ingredient in MENU[user_choice]['ingredients']:
                    resources[ingredient] -= MENU[user_choice]['ingredients'][ingredient]
                sleep(2)
                cls()

turn_on()
            
    

    

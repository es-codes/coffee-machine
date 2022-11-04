from utils.menu import MENU, resources
import os

def cls():
    '''clear the screen'''
    os.system('cls' if os.name=='nt' else 'clear')


def check_resources(drink):
    '''Checks if there is enough resources
     for the drink'''
    if MENU[drink]['ingredients']['water'] > resources['water']:
        return 'Sorry, we are out of enough water'
    elif MENU[drink]['ingredients']['coffee'] > resources['coffee']:
        return 'Sorry, we are out of enough coffee'
    elif MENU[drink]['ingredients']['milk'] > resources['milk']:
        return 'Sorry, we are out of enough milk'

def coin_processor(quarters, dimes, nickles, pennies):
    '''Process the money received, returning the sum'''
    sum_quarters = quarters * 0.25
    sum_dimes = dimes * 0.10
    sum_nickles = nickles * 0.05
    sum_pennies = pennies * 0.01
    return sum_quarters + sum_dimes + sum_nickles + sum_pennies

def transaction(money, user_choice):
    '''Makes the transaction between machine and the user'''
    if money < MENU[user_choice]['cost']:
        return f'Sorry, thats not enough money. Money refunded.'
    elif money > MENU[user_choice]['cost']:
        change = money - MENU[user_choice]['cost']
        resources['Money'] = MENU[user_choice]['cost']
        return f'Here is ${change:.2f} dollars in change. Thank you for your choice!'
    else:
        resources['Money'] = money
        return 'Thank you for your choice!'
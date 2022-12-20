import os
from order import order




def welcome():
    os.system('cls')
    print("Welcome to QA Cafe!")
    return

def main_menu():
    choice = int(input("what do you want to do? \n\n 1. Enter an order \n 2. Read an order \n 3. Read all orders \n 4. Update an order by id \n 5. Delete an order by id \n 6. Delete all orders \n\n Option: "))

    if choice == 1:
        simple_order()
    elif choice == 2:
        read_order()
    elif choice == 3:
        read_all_orders()
    elif choice == 4:
        update_order()
    elif choice == 5:
        delete_order()
    elif choice == 6:
        delete_all()
    else: 
        print ("Incorrect Response. Try again")
        main_menu()

def simple_order():
    customer_name=input("Please input your name: ")
    drink=input("Please select your drink: ")
    size=input("What size? ")
    cream=input("Cream?")
    order = order(customer_name, drink, size, cream)
    print (order)




welcome()
main_menu()





# beans = ["Colombia", "Brazil", "Java", "Guatamala"]
# drink = ["Americano", "Cappucino", "Latte"]
# size = ["Small", "Medium", "Large"]
# syrup = ["Vanilla", "cinnamon", "orange", "none"]
# sprinkles = [True, False]
# cream = [True, False]
# def order():
#     print("\n ORDER \n")
#     bean_choice = input(f"Please select your bean source: \n 1. {beans[0]} \n 2. {beans[1]} \n 3. {beans[2]} \n 4. {beans[3]} \n\n")
#     drink_choice = input(f"\n Please select type: \n 1. {drink[0]} \n 2. {drink[1]} \n 3. {drink[2]} \n\n")
#     size_choice = input(f"\n Please select size: \n 1. {size[0]} \n 2. {size[1]} \n 3. {size[2]} \n\n")
#     syrup_choice = input(f"\n Please select syrup: \n 1. {syrup[0]} \n 2. {syrup[1]} \n 3. {syrup[2]} \n 4. {syrup[3]} \n")
#     sprinkles_choice = input("\n Do you want chocolate sprinkles? y/n: \n")
#     cream_choice = input("\n Do you want whipped cream with that? y/n \n")

#     print(f"To confirm, your order is a {beans.bean_choice} sourced {size_choice} {drink_choice} with {syrup_choice} syrup, {sprinkles_choice} sprinkles and {cream_choice} cream.")
#     confirm = input("\n Is this correct?")
# 2







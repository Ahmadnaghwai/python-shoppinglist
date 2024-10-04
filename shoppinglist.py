# shoppinglist.py
shoppinglist = []
def add_item():
    item = input("Please enter the item to add to the shopping list: ")
    shoppinglist.append(item)
    print(f"{item} has been added to the shopping list.")


def show_shoppinglist():
    if shoppinglist:
        print("Your shopping list:")
        for item in shoppinglist:
            print(f"- {item}")
    else:
        print("Your shopping list is empty.")

def main():
    while True:
        print("\n----- Shopping List -----")
        print("1. Add item to shopping list")
        print("2. Show shopping list")
        print("3. Exit program")

        choice = input("Please select an option (1, 2, or 3): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            show_shoppinglist()
        elif choice == '3':
            print("Program will exit! Goodbye.")
            break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")

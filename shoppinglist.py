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
